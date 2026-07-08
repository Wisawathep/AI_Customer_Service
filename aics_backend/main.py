import time
from groq import Groq
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from config import settings
from database import conn, cursor
from security import is_attack
from rag.retrieval.retriever import Retriever
from rag.prompts.prompt_builder import PromptBuilder
from rag.prompts.system_prompt import SYSTEM_PROMPT
from rag.guardrails.input_guardrail import check_input
from rag.guardrails.retrieval_guardrail import retrieval_guardrail
from rag.guardrails.output_guardrail import output_guardrail
from rag.guardrails.context_validator import validate_context
from llm_logging.logger import PipelineLogger

class ChatRequest(BaseModel):
    session_id: str
    message: str

app = FastAPI()
logger = PipelineLogger()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=settings.GROQ_API_KEY)
retriever = Retriever()
prompt_builder = PromptBuilder()

@app.get("/logs")
def get_logs():
    return logger.get_logs()

@app.post("/chat")
async def chat(request: ChatRequest):

    logger.reset()
    logger.set_question(request.message)

    if is_attack(request.message):
        return {
            "ขออภัย ไม่สามารถยืนยันคำตอบจากฐานความรู้ได้"
        }
    
    # -----------------------------
    # Input Guardrail
    # -----------------------------

    valid, message = check_input(request.message)
    logger.log_input_guardrail(
        status="PASS" if valid else "FAIL",
        reason=message
    )
    if not valid:
        return {
            "answer": message
    }
    # -----------------------------
    # Save User Message
    # -----------------------------
    cursor.execute(
        """
        INSERT INTO chat_messages
        (session_id, role, message)
        VALUES (%s,%s,%s)
        """,
        (
            request.session_id,
            "user",
            request.message,
        ),
    )
    conn.commit()

    # -----------------------------
    # Load Chat History
    # -----------------------------
    cursor.execute(
        """
        SELECT role, message
        FROM (
            SELECT id, role, message
            FROM chat_messages
            WHERE session_id=%s
            ORDER BY id DESC
            LIMIT 20
        ) t
        ORDER BY id ASC
        """,
        (request.session_id,),
    )

    history = cursor.fetchall()

    # -----------------------------
    # Retrieve Knowledge
    # -----------------------------
    retrieved_chunks = retriever.retrieve(
        request.message,
        top_k=5,
    )

    logger.log_retriever(retrieved_chunks)

    ## -----------------------------
    ## Retrieval Guardrail
    ## -----------------------------

    before = len(retrieved_chunks)
    after = before

    logger.log_retrieval_guardrail(
        before=before,
        after=after,
        status="SKIPPED",
        reason="Disabled"
    )


    # -----------------------------
    # Build Prompt
    # -----------------------------
    context = prompt_builder.build_context(
    retrieved_chunks
    )
                
    prompt = prompt_builder.build(
        question=request.message,
        context=context,
    )

    logger.log_prompt_builder(prompt)

    # -----------------------------
    # Messages
    # -----------------------------
    messages = [
                    {
                        "role": "system",
                        "content": prompt,
                    }
    ]

    for role, message in history:
        messages.append(
            {
                "role": role,
                "content": message,
            }
        )

    # -----------------------------
    # Call Groq
    # -----------------------------
    logger.start_llm()
    response = client.chat.completions.create(
        model=settings.LLM_MODEL,
        messages=messages,
        temperature=settings.TEMPERATURE,
        max_completion_tokens=settings.MAX_TOKENS,
        top_p=settings.TOP_P,
        stream=True,
    )

    # -----------------------------
    # Streaming Response
    # -----------------------------
    def generate():

        answer = ""

        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                answer += content
        logger.set_answer(answer)

        passed = output_guardrail(
            request.message,
            context,
            answer
        )

        logger.log_output_guardrail(
            question=request.message,
            context=context,
            answer=answer,
            status="PASS" if passed else "FAIL",
            reason="Answer is valid" if passed else "Answer is not valid"
        )

        if not passed:
            answer = "ขออภัย ไม่สามารถยืนยันคำตอบจากฐานความรู้ได้"

        for ch in answer:
            time.sleep(0.01)
            yield ch

        cursor.execute(
            """
            INSERT INTO chat_messages
            (session_id, role, message)
            VALUES (%s,%s,%s)
            """,
            (
                request.session_id,
                "assistant",
                answer,
            ),
        )

        conn.commit()

    return StreamingResponse(
        generate(),
        media_type="text/plain",
    )