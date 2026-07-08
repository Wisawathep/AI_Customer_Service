class RAGPipeline:

    def ask(self, question):

        chunks = self.retriever.retrieve(question)

        prompt = self.prompt_builder.build(
            question,
            chunks
        )

        answer = self.llm.generate(prompt)

        return answer