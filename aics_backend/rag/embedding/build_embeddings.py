import json
from pathlib import Path
from rag.embedding.embedding_manager import EmbeddingManager
from rag.embedding.vector_store import VectorStore


CHUNK_PATH = Path("rag/chunked_data")

def build_embeddings():

    embedder = EmbeddingManager()
    store = VectorStore()
    total = 0

    for file in CHUNK_PATH.glob("*_chunks.json"):

        print(f"Reading {file.name}")
        with open(file, "r", encoding="utf-8") as f:
            chunks = json.load(f)

        for chunk in chunks:
            embedding = embedder.embed_document(
                chunk["content"]
            )

            store.add_chunk(
                chunk,
                embedding
            )

            total += 1

    print("=" * 40)
    print(f"Embedded {total} chunks")

if __name__ == "__main__":
    build_embeddings()