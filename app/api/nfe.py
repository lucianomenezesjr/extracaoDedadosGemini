from fastapi import APIRouter
from app.services.gemini_service import simular_extracao

router = APIRouter()

@router.post("/processar")
def processar_nfe():
    dados = simular_extracao()
    return {"mensagem": "Dados extraídos com sucesso", "dados": dados}
