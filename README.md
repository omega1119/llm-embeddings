# PDF Embeddings Semantic Search and Conversational Chat

This project enables efficient **semantic search** and interactive **conversational querying** across multiple PDF documents using OpenAI embeddings, FAISS vector search, and LangChain with continuous conversation support.

---

## 🚀 Features

- **Semantic Search** across multiple PDF documents
- **Conversational Chat** with memory and contextual continuity
- **Local Embeddings Storage** using FAISS for efficient offline access
- Interactive notebooks via Jupyter or VS Code
- Automatic support for **mathematical and physics calculations** within conversations

---

## 🛠 Setup Instructions

### 1. Conda Environment

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

### 3. Configure OpenAI API Key

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
│   ├── database.py                # SQLite chunk storage
│   └── embeddings.py              # Embeddings and FAISS management
│
├── notebooks/                     # Interactive notebooks
│   ├── build.ipynb                # Process PDFs and build embeddings
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

Open `notebooks/build.ipynb` and update PDF folders:

```python
build_faiss_index(
        ["./pdf_folder1", "./pdf_folder2"], 
        chunk_size=800
    )
```

Run all cells sequentially to:

- Extract and chunk texts from PDFs
- Store chunks in SQLite (`chunks.db`)
- Generate embeddings and store them in FAISS

### Chunk Size Configuration

Adjust chunk size in your `build_faiss_index` method to optimize embeddings:

| Chunk Size (words)    | Recommended Use                              |
| --------------------- | -------------------------------------------- |
| `100-300`             | Fine-grained, specific info, short texts     |
| `500-800` *(default)* | Good balance between context and granularity |
| `1000-1500`           | More context-rich, larger documents          |

Example:

```python
build_faiss_index(["path/to/pdf"], chunk_size=500)
```

### Step 3: Perform Queries

Use `notebooks/query.ipynb` for direct semantic searches.

Example query:

```python
query = "Explain cosmological redshift."
```

### Step 4: Conversational Chat with Calculations

Open `notebooks/chat.ipynb`:

Set up the chat explicitly:

```python
from pdfchat import setup_chat, chat, clear_memory

setup_chat()
```

Start interactive conversations:

```python
chat("What is cosmological redshift?")

# Conversational follow-up:
chat("Explain what 'z' represents.")
```

Clear conversation memory when needed:

```python
clear_memory()
```

---

## 📚 References

- [Semantic Search with LangChain & OpenAI](https://www.youtube.com/watch?v=h0DHDp1FbmQ)
- [LangChain "Ask A Book" Example](https://github.com/gkamradt/langchain-tutorials/blob/main/data_generation/Ask%20A%20Book%20Questions.ipynb)
- [Sample PDFs (py-pdf)](https://github.com/py-pdf/sample-files)
- [Sample PDFs (tpn)](https://github.com/tpn/pdfs)
- [PDF Cabinet of Horrors](https://github.com/openpreserve/format-corpus/tree/master/pdfCabinetOfHorrors)
- [Format Corpus Sample Files](https://github.com/openpreserve/format-corpus)

---

## 📜 License

Provided **as-is** for educational purposes. Feel free to modify, extend, and share!
