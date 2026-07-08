from rag.loader import DocumentLoader
from rag.chunkers.chunk_manager import ChunkManager
from rag.utils.save_chunks import save_chunks


KNOWLEDGE_PATH = "../knowledge"


def build_chunks():

    loader = DocumentLoader(KNOWLEDGE_PATH)
    documents = loader.load_txt()

    manager = ChunkManager()

    total_chunks = 0

    for document in documents:

        print(f"Processing: {document.filename}")

        chunks = manager.chunk(document)

        save_chunks(
            chunks,
            f"{document.category}_chunks.json"
        )

        total_chunks += len(chunks)

        print(f"✓ {len(chunks)} chunks created")

    print("\n========== Finished ==========")
    print(f"Total Documents : {len(documents)}")
    print(f"Total Chunks    : {total_chunks}")


if __name__ == "__main__":
    build_chunks()