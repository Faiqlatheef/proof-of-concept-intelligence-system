from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from rag.ingest import ingest_pdf
from rag.query import answer_query

app = FastAPI()

# 🔑 CORS: allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ingest")
async def ingest(files: list[UploadFile]):
    for f in files:
        ingest_pdf(f)
    return {"status": "documents ingested"}

@app.post("/query")
async def query(payload: dict):
    return answer_query(payload["question"])
