import os
import fitz
import glob
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from tqdm import tqdm
from .config import EMBEDDING_MODEL, FAISS_INDEX_DIR
from .database import store_chunks, init_db

def extract_pdf_text(pdf_path):
    doc = fitz.open(pdf_path)
    return ''.join(page.get_text() for page in doc)

def chunk_text(text, chunk_size=500):
    words = text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def process_pdfs(root_folders, chunk_size=500):
    chunks, sources = [], []
    for folder in root_folders:
        pdf_files = glob.glob(os.path.join(folder, "**/*.pdf"), recursive=True)
        for pdf in pdf_files:
            text = extract_pdf_text(pdf)
            # Explicitly adjustable chunk size here
            pdf_chunks = chunk_text(text, chunk_size=chunk_size)
            chunks.extend(pdf_chunks)
            sources.extend([pdf] * len(pdf_chunks))
    return chunks, sources


def build_faiss_index(root_folders, batch_size=100, chunk_size=500):
    embeddings_model = OpenAIEmbeddings(model=EMBEDDING_MODEL)

    # explicitly pass chunk_size
    chunks, sources = process_pdfs(root_folders, chunk_size=chunk_size)
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
