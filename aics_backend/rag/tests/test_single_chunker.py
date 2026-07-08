from rag.loader import DocumentLoader
from rag.chunkers.chunk_manager import ChunkManager

loader = DocumentLoader("../knowledge")
documents = loader.load_txt()

manager = ChunkManager()

single_document = next(
    doc for doc in documents
    if doc.category == "policy"
)

chunks = manager.chunk(single_document)

print(f"Document : {single_document.filename}")
print(f"Chunks : {len(chunks)}")

for chunk in chunks:

    print("-" * 60)
    print(chunk.metadata)
    print(chunk.content)