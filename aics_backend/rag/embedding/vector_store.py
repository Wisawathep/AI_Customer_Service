import chromadb

class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="rag/vector_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="petshop_knowledge"
        )

    def add_chunk(self, chunk, embedding):

        self.collection.add(
            ids=[chunk["id"]],
            documents=[chunk["content"]],
            embeddings=[embedding],
            metadatas=[chunk["metadata"]]
        )
        
    def search(self, query_embedding, top_k=3):

        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=[
                "documents",
                "metadatas",
                "distances"
            ]
        )