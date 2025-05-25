# PDF Embeddings Semantic Search and Conversational Chat

This project enables efficient **semantic search** and **conversational querying** across multiple PDF documents using OpenAI embeddings, FAISS vector search, and LangChain for continuous conversational context.

---

## 🚀 Features

- **Semantic Search** across multiple PDFs
- **Conversational Chat** with memory and context management
- **Local Embeddings Storage** for efficient offline access using FAISS
- Interactive interface via Jupyter Notebooks or VS Code

---

## 🛠 Setup Instructions

### 1. Conda Environment

Create and activate the `llm_embeddings` Conda environment (Python 3.11 recommended):

```bash
conda create -n llm_embeddings python=3.11 -y
conda activate llm_embeddings
```

### 2. Install Dependencies

Install required Python packages:

```bash
pip install openai PyMuPDF faiss-cpu python-dotenv langchain langchain-openai langchain-community
```

### 3. OpenAI API Key

Create a `.env` file in your project directory containing your OpenAI API key:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## Project Structure

```bash
project_folder/
├── build.ipynb              # Process PDFs and generate embeddings
├── query.ipynb              # Semantic search and query interface
├── chat.ipynb               # Interactive conversational chat notebook
├── chunks.db                # SQLite database with PDF text chunks
└── faiss_index_directory/   # FAISS vectorstore (embeddings and metadata)
    ├── index.faiss
    └── index.pkl
```

## ▶️ Usage
### Step 1: Prepare PDF Documents

In build.ipynb, update the list of PDFs you wish to process:

```python
pdf_files = ["document1.pdf", "document2.pdf"]  # Replace with your PDFs
```

### Step 2: Generate Embeddings
Run cells sequentially in `build.ipynb` to:

- Extract text from PDFs.
- Create and store embeddings locally using FAISS.
- Save document chunks and metadata.

### Step 3: Query Documents
For quick semantic queries, use `query.ipynb`.

For conversational interactions with memory context, use `chat.ipynb`.

## 💬 Conversational Chat with Memory
In `chat.ipynb`, engage in continuous dialogue:

```python
chat("Explain cosmological redshift.")

# Follow-up questions use previous context automatically:
chat("What does the variable 'z' represent?")
```

Clear conversation memory if needed:

```python
memory.clear()
```

## 📚 References

* [Video Tutorial](https://www.youtube.com/watch?v=h0DHDp1FbmQ)
* [LangChain Ask A Book Example](https://github.com/gkamradt/langchain-tutorials/blob/main/data_generation/Ask%20A%20Book%20Questions.ipynb)

## License

This project is provided as-is for educational purposes. Modify and extend as needed!