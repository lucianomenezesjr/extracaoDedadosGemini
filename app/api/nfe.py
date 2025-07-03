from fastapi import APIRouter
from app.services.gemini_service import GeminiService

router = APIRouter()
gemini_service = GeminiService()

@router.get("/test-gemini")
async def test_gemini(prompt: str = "Explique como funciona a API do Gemini em 2 frases"):
    response = gemini_service.generate_text(prompt)
    return {"prompt": prompt, "response": response}

@router.get("/list-models")
def list_models():
    service = GeminiService()
    return service.list_models()