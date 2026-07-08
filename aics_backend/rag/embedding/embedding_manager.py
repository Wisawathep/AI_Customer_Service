from sentence_transformers import SentenceTransformer

class EmbeddingManager:

    def __init__(self):
        self.model = SentenceTransformer(
            "BAAI/bge-m3"
        )

    def embed_document(self, text: str):
        return self.model.encode(
            text,
            normalize_embeddings=True,
            prompt_name="document").tolist()
    
    def embed_query(self, text: str):
        return self.model.encode(
            text,
            normalize_embeddings=True,
            prompt_name="query"
        ).tolist()