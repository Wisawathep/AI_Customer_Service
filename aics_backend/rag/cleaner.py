import re

class TextCleaner:
    @staticmethod
    def clean(text: str) -> str:
        """
        Clean raw document text before chunking.
        """
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")
        text = "\n".join(line.strip() for line in text.split("\n"))
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = text.strip()

        return text