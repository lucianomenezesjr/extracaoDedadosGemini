# app/services/gemini_service.py

import os
import mimetypes
from dotenv import load_dotenv
import google.generativeai as genai

from app.database import SessionLocal
from app.models.receipt import Receipt
from datetime import datetime

class GeminiService:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")

        genai.configure(api_key=api_key)

        
        self.model = genai.GenerativeModel('models/gemini-1.5-flash')

    def generate_from_file(self, file_path: str, prompt: str = "Extract CNPJ, data of emission and total value."):
        try:
            mime_type, _ = mimetypes.guess_type(file_path)

            with open(file_path, "rb") as f:
                file_data = f.read()

            file_part = {
                "mime_type": mime_type or "application/pdf",
                "data": file_data
            }

            response = self.model.generate_content([
                prompt,
                file_part
            ])

            result_text = response.text

            import json
            import re

            json_text = re.sub(r"```json|```", "", result_text).strip()

            try:
                parsed = json.loads(json_text)

                cnpj = parsed.get("cnpj")
                date_of_emission = datetime.strptime(parsed.get("date_of_emission"), "%d/%m/%Y").date()
                total_value = float(parsed.get("total_value"))
                file_name = parsed.get("file_name", os.path.basename(file_path))
            except Exception as e:
                return f"Error while processing the returned JSON: {str(e)}"

            db = SessionLocal()
            receipt = Receipt(
                cnpj=cnpj,
                date_of_emission=date_of_emission,
                total_value=total_value,
                file_name=file_name
            )
            db.add(receipt)
            db.commit()
            db.close()

            return result_text

        except Exception as e:
            return f"Error while processing: {str(e)}"
