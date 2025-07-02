from fastapi import FastAPI
from app.api import nfe

app = FastAPI(title="Simulador de Nota Fiscal com Gemini")

app.include_router(nfe.router, prefix="/nfe", tags=["Notas Fiscais"])
