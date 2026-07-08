from rag.loader import DocumentLoader
from rag.chunkers.faq_chunker import FAQChunker
from rag.chunkers.chunk_manager import ChunkManager


loader = DocumentLoader("../knowledge")

documents = loader.load_txt()

faq_document = next(
    doc for doc in documents
    if doc.category == "faq"
)

manager = ChunkManager()
chunks = manager.chunk(faq_document)

print("=" * 60)
print("Document")
print("=" * 60)

print(faq_document.filename)

print()

print("=" * 60)
print("Chunks")
print("=" * 60)

for chunk in chunks:

    print(chunk.id)

    print(chunk.category)

    print(chunk.source)

    print(chunk.content)

    print("-" * 40)