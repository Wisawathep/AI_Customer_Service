from rag.embedding.embedding_manager import EmbeddingManager
from rag.embedding.vector_store import VectorStore


class Retriever:

    def __init__(self):

        self.embedder = EmbeddingManager()
        self.store = VectorStore()

    def retrieve(self, question, top_k=3):

        query_embedding = self.embedder.embed_query(question)
        result = self.store.search(query_embedding, top_k)
        retrieved = []

        documents = result["documents"][0]
        metadatas = result["metadatas"][0]
        distances = result["distances"][0]

        for doc, meta, distance in zip(documents, metadatas, distances):

            retrieved.append({
                "content": doc,
                "metadata": meta,
                "distance": distance,
                "similarity": 1 - distance
            })

        return retrieved