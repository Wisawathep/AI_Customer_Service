MAX_DISTANCE = 1.0

def retrieval_guardrail(results):

    if not results:
        return False, [], "Retriever ไม่พบข้อมูล"

    filtered = [
        chunk
        for chunk in results
        if chunk["distance"] <= MAX_DISTANCE
    ]

    if not filtered:
        return False, [], "Chunk ทั้งหมดมี Distance สูงเกินกำหนด"

    return True, filtered, "ผ่าน"