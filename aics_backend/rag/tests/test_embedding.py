from rag.embedding.embedding_manager import EmbeddingManager
from rag.embedding.vector_store import VectorStore

embedder = EmbeddingManager()
store = VectorStore()

query = "ยี่ห้ออาหารแมวมีอะไรบ้าง"

embedding = embedder.embed_query(query)

result = store.search(embedding)
print(result)
print("==============================")
print(result["documents"])