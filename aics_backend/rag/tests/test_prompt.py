from rag.prompts.prompt_builder import PromptBuilder


def test_prompt_builder_includes_question_and_context():
    builder = PromptBuilder()
    chunks = [{"content": "อาหารสำหรับลูกสุนัขควรมีโปรตีนสูง"}]

    prompt = builder.build("อาหารสำหรับลูกสุนัข", chunks)

    assert "อาหารสำหรับลูกสุนัข" in prompt
    assert "ข้อมูลอ้างอิง" in prompt
    assert "อาหารสำหรับลูกสุนัขควรมีโปรตีนสูง" in prompt