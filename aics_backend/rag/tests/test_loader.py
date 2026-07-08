from rag.loader import DocumentLoader
from rag.cleaner import TextCleaner
from rag.chunkers.base_chunker import TextChunker

loader = DocumentLoader("knowledge")

documents = loader.load_txt()

chunker = TextChunker()

chunks = chunker.split(documents)

for chunk in chunks:

    print("=" * 50)
    print(chunk["filename"])
    print(chunk["chunk_id"])
    print(chunk["content"])