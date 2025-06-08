import sqlite3
from .config import DB_NAME

def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS chunks (
            id INTEGER PRIMARY KEY,
            source TEXT,
            chunk TEXT
        )
    """)
    conn.commit()
    return conn

def store_chunks(conn, chunks, sources):
    conn.executemany(
        "INSERT INTO chunks (source, chunk) VALUES (?, ?)", 
        zip(sources, chunks)
    )
    conn.commit()

def get_total_chunks(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM chunks")
    total = cursor.fetchone()[0]
    return total

def fetch_chunks_batch(conn, offset, limit):
    cursor = conn.cursor()
    cursor.execute(
        "SELECT chunk, source FROM chunks LIMIT ? OFFSET ?", (limit, offset)
    )
    return cursor.fetchall()
