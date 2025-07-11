import os
import mimetypes
import json
import re
from dotenv import load_dotenv
import google.generativeai as genai
from datetime import datetime
from fastapi import HTTPException

from app.database import SessionLocal
from app.models.receipt import Receipt

class GeminiService:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('models/gemini-1.5-flash')

    def generate_from_file(self, file_path: str):
        try:
            mime_type, _ = mimetypes.guess_type(file_path)
            
            with open(file_path, "rb") as f:
                file_data = f.read()

            prompt = """Por favor, analise este documento e extraia as seguintes informações em formato JSON:
            {
                "cnpj": "CNPJ da empresa no formato XX.XXX.XXX/XXXX-XX",
                "date_of_emission": "Data de emissão no formato DD/MM/YYYY",
                "total_value": "Valor total como número decimal",
                "file_name": "Nome do arquivo original"
            }
            Retorne APENAS o JSON, sem nenhum texto adicional ou comentários."""

            response = self.model.generate_content([prompt, {
                "mime_type": mime_type or "application/pdf",
                "data": file_data
            }])

            # Limpar a resposta para extrair apenas o JSON
            json_text = re.sub(r'^[^{]*', '', response.text)  # Remove tudo antes do {
            json_text = re.sub(r'[^}]*$', '', json_text)      # Remove tudo depois do }
            json_text = json_text.strip()

            try:
                parsed = json.loads(json_text)
                
                # Validar campos obrigatórios
                required_fields = ['cnpj', 'date_of_emission', 'total_value']
                for field in required_fields:
                    if field not in parsed:
                        raise ValueError(f"Campo obrigatório '{field}' não encontrado")

                cnpj = parsed['cnpj']
                date_of_emission = datetime.strptime(parsed['date_of_emission'], "%d/%m/%Y").date()
                total_value = float(parsed['total_value'])
                file_name = parsed.get('file_name', os.path.basename(file_path))

            except (json.JSONDecodeError, ValueError, KeyError) as e:
                raise HTTPException(
                    status_code=400,
                    detail=f"Resposta do Gemini em formato inválido. Erro: {str(e)}. Resposta recebida: {response.text}"
                )

            # Salvar no banco de dados
            db = SessionLocal()
            try:
                receipt = Receipt(
                    cnpj=cnpj,
                    date_of_emission=date_of_emission,
                    total_value=total_value,
                    file_name=file_name
                )
                db.add(receipt)
                db.commit()
                db.refresh(receipt)

                return {
                    "id": receipt.id,
                    "cnpj": receipt.cnpj,
                    "date_of_emission": receipt.date_of_emission.strftime("%d/%m/%Y"),
                    "total_value": receipt.total_value,
                    "file_name": receipt.file_name,
                    "created_at": receipt.created_at.strftime("%Y-%m-%d %H:%M:%S")
                }
            finally:
                db.close()

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Erro ao processar arquivo: {str(e)}"
            )