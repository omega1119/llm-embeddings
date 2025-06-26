# PDF Embeddings Semantic Search and Conversational Chat

This project enables efficient **semantic search** and interactive **conversational querying** across multiple document formats (PDF, PPTX, DOCX, Python scripts, Jupyter notebooks) using **OpenAI embeddings**, **FAISS vector search**, **SQLite chunk storage**, and **LangChain** with continuous conversation support. It leverages **Retrieval-Augmented Generation (RAG)**, where the conversational agent is augmented with context retrieved from a file store to provide intelligent, context-aware responses.

---

## 🚀 Features

* **Semantic Search** across PDFs, Word docs, PPTX files, Python scripts, and Jupyter notebooks.
* **Conversational Chat** with memory and contextual continuity, enabling natural conversations.
* **Local Embeddings Storage** using **FAISS** for efficient offline access to semantic vectors.
* Integrates **Retrieval-Augmented Generation (RAG)** to combine document retrieval with conversational responses powered by **OpenAI GPT models**.
* **Mathematical and Physics Calculations**: Built-in support for complex calculations and formulas within conversations.
* **OCR Support**: Automatically extracts text from images embedded in PDFs using **Tesseract OCR**.
* **LangChain Compatibility**: Seamlessly integrate with **LangChain** for advanced document query handling and chat applications.

---

## 🛠 Setup Instructions

### 1. Create Conda Environment

Create and activate the Conda environment (`llm_embeddings`):

```bash
conda create -n llm_embeddings python=3.11 -y
conda activate llm_embeddings
```

### 2. Install Dependencies

Install necessary packages using pip:

```bash
pip install -r requirements.txt
pip install -e .
```

### 3. Install Tesseract OCR (for PDF OCR support)

* **macOS** (with Homebrew):

```bash
brew install tesseract
```

* **Ubuntu/Linux**:

```bash
sudo apt-get install tesseract-ocr
```

### 4. Configure OpenAI API Key

Create a `.env` file containing your OpenAI API key:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 📂 Project Structure

```
project_folder/
├── pdfchat/                       # Core library modules
│   ├── __init__.py
│   ├── chat.py                    # Conversational chat module
│   ├── config.py                  # Configuration parameters
│   ├── database.py                # SQLite chunk storage utilities
│   └── embeddings.py              # Embeddings and FAISS management
│
├── notebooks/                     # Interactive notebooks
│   ├── build.ipynb                # Process files and build embeddings
│   ├── query.ipynb                # Direct semantic querying
│   └── chat.ipynb                 # Conversational chat interface
│
├── faiss_index_directory/         # FAISS vectorstore (generated)
│   ├── index.faiss
│   └── index.pkl
│
├── chunks.db                      # SQLite database (generated)
├── setup.py                       # Installation setup file
├── requirements.txt               # Project dependencies
├── .env                           # OpenAI API configuration
└── README.md                      # Project documentation
```

---

## 🚩 How to Run the Project

### Step 1: Install the Project

Ensure you're in the project root folder and install the library in editable mode:

```bash
pip install -e .
```

### Step 2: Generate Embeddings and Chunks

Open `notebooks/build.ipynb` and update your file folders explicitly:

```python
from pdfchat import build_faiss_index

build_faiss_index(
    ["./docs_folder1", "./docs_folder2"], 
    chunk_size=800,
    exclusions=["archive", ".git"],
    rebuild_chunks=True
)
```

Run all cells sequentially to:

* Extract and chunk texts from supported files.
* Store chunks in SQLite (`chunks.db`).
* Generate embeddings and store them in FAISS (`faiss_index_directory`).

### Chunk Size Configuration

Adjust chunk size in your `build_faiss_index` method to optimize embeddings:

| Chunk Size (words)    | Recommended Use                              |
| --------------------- | -------------------------------------------- |
| `100-300`             | Fine-grained, specific info, short texts     |
| `500-800` *(default)* | Good balance between context and granularity |
| `1000-1500`           | More context-rich, larger documents          |

Example explicitly:

```python
build_faiss_index(["path/to/documents"], chunk_size=500)
```

### Batch Size Configuration

Adjust batch size in your `build_faiss_index` method to control how many chunks are processed simultaneously:

| Batch Size (chunks)  | Recommended Use                                |
| -------------------- | ---------------------------------------------- |
| `50-100` *(default)* | Good balance of RAM usage and processing speed |
| `10-50`              | Lower RAM usage, slower processing             |
| `200-500`            | Higher RAM usage, faster processing            |

Example explicitly:

```python
build_faiss_index(["path/to/documents"], batch_size=100)
```

### Step 3: Perform Queries

Use `notebooks/query.ipynb` for direct semantic searches:

```python
query = "Explain cosmological redshift."
```

### Step 4: Conversational Chat with Calculations

Open `notebooks/chat.ipynb` and explicitly set up the chat system:

```python
from pdfchat import setup_chat, chat, clear_memory

setup_chat()
```

Start interactive conversations:

```python
chat("What is cosmological redshift?")
chat("Explain what 'z' represents.")
```

Clear conversation memory explicitly when needed:

```python
clear_memory()
```

---

## 🔄 Rebuilding Indexes and Chunks

### Full rebuild (chunks + FAISS index):

```python
build_faiss_index(
    ["./docs_folder"], 
    rebuild_chunks=True
)
```

### Rebuild only FAISS index (from existing chunks.db):

```python
build_faiss_index(rebuild_chunks=False)
```

---

## 📚 Supported File Types

| File type | Extraction method                  | Library              |
| --------- | ---------------------------------- | -------------------- |
| `.pdf`    | Text extraction + OCR (for images) | PyMuPDF, PyTesseract |
| `.py`     | Direct text extraction             | Built-in Python      |
| `.ipynb`  | Notebook cell extraction           | nbformat             |
| `.pptx`   | Slide text extraction              | python-pptx          |
| `.docx`   | Paragraph text extraction          | python-docx          |

---

## 📚 Useful References

* [Semantic Search with LangChain & OpenAI](https://www.youtube.com/watch?v=h0DHDp1FbmQ)
* [LangChain "Ask A Book" Example](https://github.com/gkamradt/langchain-tutorials/blob/main/data_generation/Ask%20A%20Book%20Questions.ipynb)
* [PyMuPDF Documentation](https://pymupdf.readthedocs.io/)
* [PyTesseract OCR](https://github.com/madmaze/pytesseract)
* [python-pptx](https://python-pptx.readthedocs.io/)
* [python-docx](https://python-docx.readthedocs.io/)
* [Sample PDFs (py-pdf)](https://github.com/py-pdf/sample-files)

---

## 📜 License

Provided **as-is** for educational purposes. Feel free to modify, extend, and share!
