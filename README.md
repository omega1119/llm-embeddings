# PDF Embeddings Semantic Search

This project allows you to perform semantic search across multiple PDF documents using OpenAI embeddings and FAISS for efficient local search. Answers to queries are generated using ChatGPT based on relevant extracted document chunks.

## Setup

### 1. Create and Activate Conda Environment

Create a new Conda environment named `llm_embeddings` with Python 3.11 (or your preferred version):

```bash
conda create -n llm_embeddings python=3.11 -y
conda activate llm_embeddings
```

### 2. Install Dependencies

Run the following command to install necessary dependencies:

```bash
pip install openai PyMuPDF faiss-cpu numpy python-dotenv
```

### 3. OpenAI API Key

Create a `.env` file in the project directory and add your OpenAI API key:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## Project Structure

* `main.ipynb`: Jupyter notebook containing the core implementation.
* `chunks.db`: SQLite database to store text chunks extracted from PDFs.
* `faiss.index`: FAISS index file storing the embeddings.

## How to Use

1. Update the PDF files in the notebook (`main.ipynb`) under the variable:

```python
pdf_files = ["document1.pdf", "document2.pdf"]
```

2. Run the notebook cells sequentially:

   * Extract and chunk PDF texts.
   * Generate embeddings and store locally.
   * Perform semantic search queries interactively.

## References

* [Video Tutorial](https://www.youtube.com/watch?v=h0DHDp1FbmQ)
* [LangChain Ask A Book Example](https://github.com/gkamradt/langchain-tutorials/blob/main/data_generation/Ask%20A%20Book%20Questions.ipynb)

## License

This project is provided as-is for educational purposes. Modify and extend as needed!
