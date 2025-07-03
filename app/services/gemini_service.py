import os
from dotenv import load_dotenv
import google.generativeai as genai

from app.database import SessionLocal  # Importa sessão do banco
from app.models.gemini_message import GeminiMessage  # Importa o modelo

class GeminiService:
    def __init__(self):

        load_dotenv()  
        api_key = os.getenv("GEMINI_API_KEY")
        
        if not api_key:
            raise ValueError("GEMINI_API_KEY não encontrada no arquivo .env")
            
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('models/gemini-1.5-flash')

    def generate_text(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            text = response.text
            
            # Registra no banco
            db = SessionLocal()
            message = GeminiMessage(prompt=prompt, response=text)
            db.add(message)
            db.commit()
            db.close()

            return response.text
        except Exception as e:
            return f"Erro ao gerar texto: {str(e)}"

    def list_models(self):
        return [model.name for model in genai.list_models()] 
