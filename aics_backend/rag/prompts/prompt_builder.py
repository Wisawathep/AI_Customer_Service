from rag.prompts.system_prompt import SYSTEM_PROMPT


class PromptBuilder:

    def build_context(self, retrieved_chunks):
        contexts = []
        for chunk in retrieved_chunks or []:
            content = (
                chunk.get("content", "")
                if isinstance(chunk, dict)
                else str(chunk)
            )

            contexts.append(content)

        if not contexts:
            return "ไม่พบข้อมูลที่เกี่ยวข้องในฐานความรู้"

        return "\n\n------------------------\n\n".join(contexts)

    def build(self, question, context):
        return f"""
                {SYSTEM_PROMPT}

                ========================
                Knowledge Base
                ========================

                {context}

                ========================

                คำถามของผู้ใช้:
                {question}
                """