from rag.loader import DocumentLoader
from rag.chunkers.chunk_manager import ChunkManager

loader = DocumentLoader("../knowledge")
documents = loader.load_txt()

manager = ChunkManager()

multi_document = next(
    doc for doc in documents
    if doc.category == "service"
)

chunks = manager.chunk(multi_document)

print("=" * 60)
print(multi_document.filename)
print(f"Document : {multi_document.filename}")
print(f"Chunks : {len(chunks)}")
print("=" * 60)
print()

for chunk in chunks:

    print(chunk.id)
    print(chunk.metadata)
    print()
    print(chunk.content)
    print("-" * 60)