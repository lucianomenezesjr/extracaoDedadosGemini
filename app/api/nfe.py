from fastapi import APIRouter, File, UploadFile, HTTPException, Query, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.services.gemini_service import GeminiService, Receipt
from app.database import SessionLocal, get_db
import tempfile
import shutil
import os

router = APIRouter()

default_prompt = """Analyze the document and extract the following information, presenting it in JSON format:

{
  "cnpj": "[CNPJ_HERE]",
  "date_of_emission": "[DD/MM/YYYY]",
  "total_value": "[NUMERIC_VALUE_HERE]",
  "file_name": "[FILE_NAME_HERE]"
}

Ensure the CNPJ is in the format XX.XXX.XXX/XXXX-XX, the emission date in DD/MM/YYYY format, and the total value as a decimal number (using dot as decimal separator).
"""

@router.post("/extract")
async def extract_fields(
    prompt: str = Query(default_prompt, description="Prompt for data extraction"), 
    file: UploadFile = File(...)):

    # Verify the supported file types
    if file.content_type not in ["application/pdf", "image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
        shutil.copyfileobj(file.file, temp_file)
        temp_path = temp_file.name

    try:
        gemini = GeminiService()
        response_text = gemini.generate_from_file(temp_path, prompt)

        return JSONResponse(content={
            "file": file.filename,
            "prompt": prompt,
            "response": response_text
        })

    finally:
        # Remove the temporary file
        os.remove(temp_path)

@router.get("/receipts")
async def get_all_receipts(db: Session = Depends(get_db)):
    """
    Returns all receipts stored in the database
    """
    try:
        receipts = db.query(Receipt).all()
        
        return [
            {
                "id": receipt.id,
                "cnpj": receipt.cnpj,
                "date_of_emission": receipt.date_of_emission.strftime("%d/%m/%Y"),
                "total_value": receipt.total_value,
                "file_name": receipt.file_name,
                "created_at": receipt.created_at.strftime("%Y-%m-%d %H:%M:%S") if receipt.created_at else None
            }
            for receipt in receipts
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error accessing database: {str(e)}")
    finally:
        db.close()