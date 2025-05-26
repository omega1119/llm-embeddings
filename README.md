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

```
conda create -n llm_embeddings python=3.11 -y
conda activate llm_embeddings
```

### 2. Install Dependencies

Install necessary packages:

```
pip install openai PyMuPDF faiss-cpu numpy python-dotenv langchain langchain-openai langchain-community langchain-experimental
```

### 3. Configure OpenAI API Key

Create a `.env` file containing your OpenAI API key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

## 📂 Project Structure

```
project_folder/
├── build.ipynb              # Process PDFs, generate embeddings, store in FAISS and SQLite
├── query.ipynb              # Semantic query interface
├── chat.ipynb               # Conversational chat notebook (with calculation support)
├── chunks.db                # SQLite database containing PDF chunks
└── faiss_index_directory/   # FAISS vectorstore for embeddings
    ├── index.faiss
    └── index.pkl
```

---

## ▶️ Usage

### Step 1: Prepare PDFs

In `build.ipynb`, define your PDF folders:

```python
root_folders = ["./pdf_folder1", "./pdf_folder2"]  # Update paths accordingly
```

### Step 2: Generate Embeddings and Chunks

Run cells sequentially in `build.ipynb` to:

- Extract and chunk texts from PDFs
- Store chunks in SQLite (`chunks.db`)
- Generate and save embeddings using FAISS

### Step 3: Perform Queries

Use `query.ipynb` for direct semantic searches.

Example:

```python
query = "Explain cosmological redshift."
```

### Step 4: Conversational Chat (with Calculations)

Use `chat.ipynb` for interactive conversations and automatic calculations.

Example conversation:

```python
chat("""
what is cosmoligical redshift?
""")

# Conversational follow-up:
chat("explain what z is?")
```

Clear memory if needed:

```python
memory.clear()
```

---

## 📚 References

- [Semantic Search with LangChain & OpenAI](https://www.youtube.com/watch?v=h0DHDp1FbmQ)
- [LangChain "Ask A Book" Example](https://github.com/gkamradt/langchain-tutorials/blob/main/data_generation/Ask%20A%20Book%20Questions.ipynb)

---

## 📜 License

Provided **as-is** for educational purposes. Feel free to modify, extend, and share!
