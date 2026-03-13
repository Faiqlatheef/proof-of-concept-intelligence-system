import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Local embedding model (no API, no quota)
model = SentenceTransformer("all-MiniLM-L6-v2")

DIMENSION = 384
index = faiss.IndexFlatL2(DIMENSION)
metadata = []

def embed(text: str) -> np.ndarray:
    # Encode and ensure correct shape + dtype for FAISS
    vec = model.encode(text)
    return np.array([vec], dtype="float32")  # shape: (1, 384)

def add_chunk(text, source, page):
    vector = embed(text)
    index.add(vector)
    metadata.append({
        "text": text,
        "source": source,
        "page": page
    })

def search(query, k=5):
    qvec = embed(query)
    _, idx = index.search(qvec, k)
    return [metadata[i] for i in idx[0]]
