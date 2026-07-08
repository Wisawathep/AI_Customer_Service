from rag.chunkers.multi_chunker import MultiSectionChunker
from rag.chunkers.single_chunker import SingleSectionChunker


class ChunkManager:

    def __init__(self):

        self.chunkers = {
            "policy": SingleSectionChunker(),
            "office_hours": SingleSectionChunker(),
            "contact": SingleSectionChunker(),
            "company": MultiSectionChunker(),
            "goods": MultiSectionChunker(),
            "service": MultiSectionChunker(),
            "payment": MultiSectionChunker(),
        }

    def chunk(self, document):

        chunker = self.chunkers.get(document.category)

        if chunker is None:
            raise ValueError(
                f"No chunker found for category '{document.category}'"
            )

        return chunker.chunk(document)