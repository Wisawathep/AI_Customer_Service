from uuid import uuid4
from rag.chunkers.base_chunker import BaseChunker
from rag.models.chunk import Chunk


class MultiSectionChunker(BaseChunker):

    def chunk(self, document):

        chunks = []
        current_lines = []
        current_title = None

        for line in document.content.splitlines():
            line = line.strip()
            if not line:
                continue

            if line.startswith("หัวข้อ :"):

                if current_lines:
                    chunks.append(
                        self._create_chunk(
                            document,
                            current_title,
                            current_lines
                        )
                    )

                current_title = line.replace("หัวข้อ :", "").strip()
                current_lines = [line]

            else:
                current_lines.append(line)

        if current_lines:
            chunks.append(
                self._create_chunk(
                    document,
                    current_title,
                    current_lines
                )
            )

        return chunks

    def _create_chunk(self, document, title, lines):

        return Chunk(
            id=str(uuid4()),
            content="\n".join(lines),
            source=document.source,
            category=document.category,
            metadata={
                "filename": document.filename,
                "title": title
            }
        )