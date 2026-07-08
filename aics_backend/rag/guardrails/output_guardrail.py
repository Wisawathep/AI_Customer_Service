from config import settings
from groq import Groq

client = Groq(api_key=settings.GROQ_API_KEY)


def output_guardrail(question, context, answer):

    prompt = f"""
            You are an AI Response Verifier.

            Your task is to verify whether the Answer is fully supported by the Context.

            Rules:
            1. Use ONLY the Context.
            2. Ignore your own knowledge.
            3. If even one factual statement in the Answer is not supported by the Context, reply NO.
            4. If the Context lacks enough information to verify the Answer, reply NO.
            5. Reply with exactly one word.

            Context:
            {context}

            Question:
            {question}

            Answer:
            {answer}

            Reply only:

            YES

            or

            NO
            """

    response = client.chat.completions.create(
        model=settings.LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        max_completion_tokens=3
    )

    verdict = response.choices[0].message.content.strip().upper()
    print("Output Guardrail:", verdict)

    return verdict.startswith("YES")