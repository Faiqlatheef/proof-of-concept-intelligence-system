import pdfplumber
import pytesseract
from pdf2image import convert_from_bytes
from rag.vector_store import add_chunk
from rag.chunking import chunk_text

def ingest_pdf(file):
    raw = file.file.read()

    try:
        with pdfplumber.open(file.file) as pdf:
            has_text = pdf.pages[0].extract_text()
    except:
        has_text = False

    if has_text:
        with pdfplumber.open(file.file) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text() or ""
                process(text, file.filename, i + 1)
    else:
        images = convert_from_bytes(raw)
        for i, img in enumerate(images):
            text = pytesseract.image_to_string(img)
            process(text, file.filename, i + 1)

def process(text, source, page):
    for chunk in chunk_text(text):
        add_chunk(chunk, source, page)