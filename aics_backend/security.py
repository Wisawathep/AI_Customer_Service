BLOCKED_KEYWORDS = [
    "system prompt",
    "prompt",
    "token",
    "api key",
    "apikey",
    "knowledge",
    "knowledge base",
    "company.txt",
    "goods.txt",
    "payment.txt",
    "policy.txt",
    "service.txt",
    "contact.txt",
    "faq.txt",
    "office_hours.txt",
    "source code",
    "database",
    "sql",
    "postgres",
    "embedding",
    "vector",
    "rag",
    "memory",
    "session",
    "groq",
    "llama",
    "context",
    "developer message"
]

def is_attack(text: str):
    text = text.lower()
    return any(
        keyword in text
        for keyword in BLOCKED_KEYWORDS
    )