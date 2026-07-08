import re

BLOCK_PATTERNS = [
    r"ignore previous",
    r"forget previous",
    r"system prompt",
    r"developer message",
    r"api key",
    r"jailbreak",
]

def check_input(query: str):

    text = query.lower()

    for pattern in BLOCK_PATTERNS:
        if re.search(pattern, text):
            return False, "ขออภัย ไม่สามารถดำเนินการตามคำขอนี้ได้"

    if len(query.strip()) < 2:
        return False, "กรุณาพิมพ์คำถามให้ชัดเจน"

    return True, None