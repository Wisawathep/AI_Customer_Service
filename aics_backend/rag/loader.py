from pathlib import Path
from rag.models.document import Document
from rag.cleaner import TextCleaner


class DocumentLoader:

    def __init__(self, knowledge_path: str):
        self.knowledge_path = Path(knowledge_path)

    def load_txt(self):

        documents = []

        for file in self.knowledge_path.rglob("*.txt"):

            with open(file, "r", encoding="utf-8") as f:

                content = TextCleaner.clean(f.read())

                documents.append(
                    Document(
                        content=content,
                        source=str(file),
                        filename=file.name,
                        category=file.stem,  
                    )
                )

        return documents