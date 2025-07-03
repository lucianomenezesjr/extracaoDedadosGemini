from fastapi import FastAPI
from app.api.nfe import router as nfe_router

app = FastAPI()

app.include_router(nfe_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "API is working!"}