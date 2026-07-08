from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    # -------------------
    # LLM
    # -------------------
    GROQ_API_KEY: str
    LLM_MODEL: str = "llama-3.1-8b-instant"
    TEMPERATURE: float = 0
    MAX_TOKENS: int = 256
    TOP_P: float = 0.1

    # -------------------
    # Embedding
    # -------------------
    EMBEDDING_MODEL: str = "BAAI/bge-m3"

    # -------------------
    # RAG
    # -------------------
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 100
    TOP_K: int = 5
    SIMILARITY_THRESHOLD: float = 0.45

    # -------------------
    # Database
    # -------------------
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    # -------------------
    # Logging
    # -------------------
    LOGGING_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()