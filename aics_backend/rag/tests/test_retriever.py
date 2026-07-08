from rag.retrieval.retriever import Retriever

retriever = Retriever()

result = retriever.retrieve(
    "อาหารสำหรับลูกสุนัข",
    top_k=3
)

print(result)