from groq import Groq
from config import settings

client = Groq(api_key=settings.GROQ_API_KEY)


def validate_context(question, context):

    prompt = f"""
คุณเป็น AI ที่ทำหน้าที่ตรวจสอบว่า Context สามารถตอบคำถามได้หรือไม่

กฎ

1. พิจารณาเฉพาะข้อมูลใน Context
2. ห้ามใช้ความรู้เดิมของโมเดล
3. หาก Context มีข้อมูลเพียงพอที่จะตอบ ให้ตอบ

YES

4. หาก Context ไม่มีข้อมูลเพียงพอ หรือจำเป็นต้องเดา ให้ตอบ

NO

========================

Context

{context}

========================

Question

{question}

========================

ตอบเพียงคำเดียว

YES

หรือ

NO
"""

    response = client.chat.completions.create(
        model=settings.LLM_MODEL,
        temperature=0,
        max_completion_tokens=3,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response.choices[0].message.content.strip().upper()
    print("===================")
    print("Context Validator")
    print(answer)
    print("===================")
    return "YES" in answer or "yes" in answer or "Yes" in answer