from uuid import uuid4

from rag.chunkers.base_chunker import BaseChunker
from rag.models.chunk import Chunk


class SingleSectionChunker(BaseChunker):

    def chunk(self, document):

        return [
            Chunk(
                id=str(uuid4()),
                content=document.content,
                source=document.source,
                category=document.category,
                metadata={
                    "filename": document.filename
                }
            )
        ]