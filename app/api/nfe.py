# app/api/nfe.py

from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from fastapi.responses import JSONResponse
from app.services.gemini_service import GeminiService
import tempfile
import shutil
import os

router = APIRouter()

default_prompt = """Analise o documento e extraia as seguintes informações, apresentando-as no formato JSON:

{
  "cnpj": "[CNPJ_AQUI]",
  "date_of_emission": "[DD/MM/AAAA]",
  "total_value": "[VALOR_NUMERICO_AQUI]",
  "file_name": "[NOME_DO_ARQUIVO_AQUI]"
}

Certifique-se de que o CNPJ esteja no formato XX.XXX.XXX/XXXX-XX, a data de emissão no formato DD/MM/AAAA e o valor total como um número decimal (usando ponto como separador decimal).
"""

@router.post("/extract")
async def extract_fields(
    prompt: str = Query(default_prompt, description="Prompt para extração dos dados"), 
    file: UploadFile = File(...)):

    # Verify the supported file types
    if file.content_type not in ["application/pdf", "image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Tipo de arquivo não suportado")

    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
        shutil.copyfileobj(file.file, temp_file)
        temp_path = temp_file.name

    try:
        gemini = GeminiService()
        response_text = gemini.generate_from_file(temp_path, prompt)

        return JSONResponse(content={
            "arquivo": file.filename,
            "prompt": prompt,
            "resposta": response_text
        })

    finally:
        # Remove the temporary file
        os.remove(temp_path)
