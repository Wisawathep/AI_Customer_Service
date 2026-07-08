from rag.loader import DocumentLoader
from rag.chunkers.chunk_manager import ChunkManager

loader = DocumentLoader("../knowledge")
documents = loader.load_txt()

manager = ChunkManager()

total_chunks = 0

for document in documents:

    chunks = manager.chunk(document)

    total_chunks += len(chunks)

    print(
        f"{document.filename:20}"
        f"{len(chunks)} chunk(s)"
    )

print(f"\nTotal Chunks : {total_chunks}")