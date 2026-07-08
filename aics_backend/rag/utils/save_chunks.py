import json
from pathlib import Path


OUTPUT_DIR = Path("rag/chunked_data")

def save_chunks(chunks, filename):

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    json_data = []

    for chunk in chunks:
        json_data.append({
            "id": chunk.id,
            "content": chunk.content,
            "source": chunk.source,
            "category": chunk.category,
            "metadata": chunk.metadata,
        })

    with open(OUTPUT_DIR / filename, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=4)

    print(f"Saved -> {OUTPUT_DIR / filename}")