import time


class PipelineLogger:

    def __init__(self):
        self.reset()


    def reset(self):

        self.logs = {
            "question": "",
            "input_guardrail": {},
            "retriever": {},
            "retrieval_guardrail": {},
            "prompt_builder": {},
            "llm": {},
            "output_guardrail": {},
            "answer": ""
        }


    def set_question(self, question):
        self.logs["question"] = question


    def log_input_guardrail(
        self,
        status,
        reason=None
    ):

        self.logs["input_guardrail"] = {
            "status": status,
            "reason": reason
        }


    def log_retriever(
        self,
        chunks
    ):

        data = []

        for chunk in chunks:

            data.append({

                "distance": round(
                    chunk["distance"],
                    4
                ),

                "source": chunk["metadata"].get(
                    "source",
                    "-"
                ),

                "preview": chunk["content"][:200]
            })

        self.logs["retriever"] = {

            "retrieved": len(chunks),

            "chunks": data
        }


    def log_retrieval_guardrail(
        self,
        before,
        after,
        status,
        reason
    ):

        self.logs["retrieval_guardrail"] = {

            "before": before,

            "after": after,

            "status": status,

            "reason": reason
        }


    def log_prompt_builder(
        self,
        context
    ):

        self.logs["prompt_builder"] = {

            "context_length": len(context),

            "context": context
        }


    def start_llm(self):

        self.start = time.time()


    def end_llm(self):

        latency = round(
            time.time() - self.start,
            2
        )

        self.logs["llm"] = {

            "latency": latency
        }


    def log_output_guardrail(
        self,
        question=None,
        context=None,
        answer=None,
        status=None,
        reason=None,
        supported=None,
    ):

        # Support both old (supported, reason) and new keyword-based calls
        entry = {}

        if supported is not None:
            entry["supported"] = supported

        if status is not None:
            entry["status"] = status

        if reason is not None:
            entry["reason"] = reason

        if question is not None:
            entry["question"] = question

        if context is not None:
            entry["context"] = context

        if answer is not None:
            entry["answer"] = answer

        self.logs["output_guardrail"] = entry


    def set_answer(
        self,
        answer
    ):

        self.logs["answer"] = answer


    def get_logs(self):

        return self.logs
    
    def log_context_validator(self, status, reason):

        self.logs["context_validator"] = {
            "status": status,
            "reason": reason
        }