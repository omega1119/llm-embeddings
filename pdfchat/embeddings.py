import os
import shutil
import fitz
import glob
import nbformat
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from tqdm import tqdm
from .config import EMBEDDING_MODEL, FAISS_INDEX_DIR, DB_NAME
from .database import store_chunks, init_db

def extract_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    return ''.join(page.get_text() for page in doc)

def extract_python_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_notebook_text(notebook_path):
    notebook = nbformat.read(notebook_path, as_version=4)
    text = ''
    for cell in notebook.cells:
        if cell.cell_type == 'code':
            text += cell.source + '\n\n'
        elif cell.cell_type == 'markdown':
            text += cell.source + '\n\n'
    return text

def chunk_text(text, chunk_size=500):
    words = text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def is_excluded(path, exclusions):
    path_parts = set(os.path.normpath(path).split(os.sep))
    return any(exclusion in path_parts for exclusion in exclusions)


def process_files(root_folders, chunk_size=500, exclusions=None):
    if exclusions is None:
        exclusions = []

    chunks, sources = [], []
    for folder in root_folders:
        # PDFs
        pdf_files = glob.glob(os.path.join(folder, "**/*.pdf"), recursive=True)
        for pdf in pdf_files:
            if is_excluded(pdf, exclusions):
                continue
            text = extract_pdf_text(pdf)
            pdf_chunks = chunk_text(text, chunk_size=chunk_size)
            chunks.extend(pdf_chunks)
            sources.extend([pdf] * len(pdf_chunks))

        # Python scripts
        py_files = glob.glob(os.path.join(folder, "**/*.py"), recursive=True)
        for py_file in py_files:
            if is_excluded(py_file, exclusions):
                continue
            text = extract_python_text(py_file)
            py_chunks = chunk_text(text, chunk_size=chunk_size)
            chunks.extend(py_chunks)
            sources.extend([py_file] * len(py_chunks))

        # Jupyter Notebooks
        notebook_files = glob.glob(os.path.join(folder, "**/*.ipynb"), recursive=True)
        for notebook_file in notebook_files:
            if is_excluded(notebook_file, exclusions):
                continue
            text = extract_notebook_text(notebook_file)
            nb_chunks = chunk_text(text, chunk_size=chunk_size)
            chunks.extend(nb_chunks)
            sources.extend([notebook_file] * len(nb_chunks))

    return chunks, sources

def clear_previous_data():
    # Delete FAISS index directory
    if os.path.exists(FAISS_INDEX_DIR):
        shutil.rmtree(FAISS_INDEX_DIR)
        print(f"Deleted previous FAISS index at {FAISS_INDEX_DIR}")

    # Delete SQLite database
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        print(f"Deleted previous SQLite database at {DB_NAME}")

def build_faiss_index(root_folders, batch_size=100, chunk_size=500, exclusions=None):
    embeddings_model = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    clear_previous_data()

    chunks, sources = process_files(root_folders, chunk_size=chunk_size, exclusions=exclusions)
    metadata = [{"source": s} for s in sources]

    conn = init_db()
    store_chunks(conn, chunks, sources)
    conn.close()

    vectorstore = None
    for i in tqdm(range(0, len(chunks), batch_size), desc="Creating embeddings"):
        batch_chunks = chunks[i:i+batch_size]
        batch_meta = metadata[i:i+batch_size]
        if vectorstore is None:
            vectorstore = FAISS.from_texts(batch_chunks, embeddings_model, batch_meta)
        else:
            vectorstore.add_texts(batch_chunks, batch_meta)

    vectorstore.save_local(FAISS_INDEX_DIR)
