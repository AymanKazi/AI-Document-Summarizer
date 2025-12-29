from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import io
import pdfplumber

from .summarizer import summarize_text   # ✅ FIXED


app = FastAPI(title="LLM Document Summarizer")

@app.get("/")
def home():
    return {"message": "Document Summarizer API running 🚀"}

@app.post("/summarize")
async def summarize_document(file: UploadFile = File(...)):
    try:
        content = await file.read()
        text = ""

        if file.filename.endswith(".pdf"):
            with pdfplumber.open(io.BytesIO(content)) as pdf:
                for page in pdf.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted + "\n"

        elif file.filename.endswith(".txt"):
            text = content.decode("utf-8")

        else:
            return JSONResponse(
                status_code=400,
                content={"error": "Only PDF and TXT files are supported"}
            )

        if not text.strip():
            return JSONResponse(
                status_code=400,
                content={"error": "No text extracted from document"}
            )

        result = summarize_text(text)

        return JSONResponse(status_code=200, content=result)

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
