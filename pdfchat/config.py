import os
from dotenv import load_dotenv

load_dotenv()

# Base directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4.1"

# Explicitly set paths relative to BASE_DIR
FAISS_INDEX_DIR = os.path.join(BASE_DIR, "faiss_index_directory")
DB_NAME = os.path.join(BASE_DIR, "chunks.db")

# Retrieval parameter
RETRIEVER_TOP_K = 5