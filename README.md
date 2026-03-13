# Grounded Intelligence Module (Verifiable RAG)

## Overview
This project is a Proof of Concept (POC) for a Verifiable Retrieval Augmented Generation (RAG) system designed for clinical-grade question answering.

The system answers questions only when evidence exists in uploaded medical documents and explicitly refuses to answer when it does not, preventing hallucinations.

## Key Features
- Medical PDF ingestion (text + scanned PDFs with OCR)
- Evidence-backed answers with citations (document + page)
- Explicit hallucination prevention ("I don't know")
- Automated grounding validation via truth script

## Architecture Overview
PDF Upload → OCR/Text Extraction → Chunking → FAISS Vector Store → Retrieval → Gemini 2.5 Flash → Answer + Evidence

## Technology Stack
Backend: Python, FastAPI, FAISS, SentenceTransformers, Gemini 2.5 Flash, Tesseract OCR  
Frontend: React, Vite

## Running Locally

### Backend
```
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
set GEMINI_API_KEY=your_api_key
python -m uvicorn main:app --reload
```

### Frontend
```
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:5173  
Backend: http://127.0.0.1:8000

## Truth Script
Run automated grounding validation:
```
cd backend
python truth_check.py
```

## Design Philosophy
Retrieval-first, evidence-driven, and safe by default.
