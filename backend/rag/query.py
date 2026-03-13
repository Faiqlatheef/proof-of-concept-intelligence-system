from google import genai
import os
from rag.vector_store import search, index

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_INSTRUCTIONS = """
You are a clinical AI assistant.

Rules:
- Use ONLY the provided context.
- If the answer is not explicitly present, respond exactly with:
  "I don't know based on the provided documents."
- Do NOT infer, guess, or fabricate medical facts.
"""

def answer_query(question: str):
    # 🔒 Guard: no documents ingested yet
    if index.ntotal == 0:
        return {
            "answer": "I don't know based on the provided documents.",
            "evidence": []
        }

    chunks = search(question)

    # 🔒 Guard: retrieval returned nothing
    if not chunks:
        return {
            "answer": "I don't know based on the provided documents.",
            "evidence": []
        }

    context = "\n\n".join(
        f"[{c['source']} – Page {c['page']}]\n{c['text']}"
        for c in chunks
    )

    prompt = f"""
{SYSTEM_INSTRUCTIONS}

Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "answer": response.text.strip(),
        "evidence": chunks
    }
