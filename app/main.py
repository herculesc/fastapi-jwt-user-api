from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.db.base import Base
from app.models.usuario import Usuario  # ❌ falta isso
from app.db.database import engine, get_db
from app.services import usuario_service
from app.routes.usuario import router as usuario_router

# Cria tabelas no banco automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuario_router)

@app.get("/")
def root():
    return {"status": "API rodando 🚀"}

