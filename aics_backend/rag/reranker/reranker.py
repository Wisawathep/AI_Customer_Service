from sentence_transformers import CrossEncoder


class Reranker:

    def __init__(self):

        self.model = CrossEncoder(
            "BAAI/bge-reranker-v2-m3"
        )

    def rerank(
        self,
        question,
        retrieved_chunks,
        top_k=3
    ):

        if not retrieved_chunks:
            return []

        pairs = []

        for chunk in retrieved_chunks:

            pairs.append(
                (
                    question,
                    chunk["content"]
                )
            )

        scores = self.model.predict(
            pairs
        )

        ranked = []

        for chunk, score in zip(
            retrieved_chunks,
            scores
        ):

            chunk["rerank_score"] = float(score)

            ranked.append(chunk)

        ranked.sort(

            key=lambda x: x["rerank_score"],

            reverse=True
        )

        return ranked[:top_k]