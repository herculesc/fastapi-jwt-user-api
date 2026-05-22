from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.usuario import UsuarioCreate
from app.services.usuario_service import (
    criar_usuario,
    listar_usuarios,
    deletar_usuario,
    buscar_usuario,
    login
)

router = APIRouter()


@router.post("/login")
def fazer_login(email: str, senha: str, db: Session = Depends(get_db)):
    token = login(db, email, senha)

    if not token:
        return {"erro": "credenciais inválidas"}

    return {"access_token": token}

# CREATE
@router.post("/register")
def register(user: UsuarioCreate, db: Session = Depends(get_db)):
    return criar_usuario(db, user.nome, user.email, user.senha)
# READ
@router.get("/usuarios")
def listar(db: Session = Depends(get_db)):
    return listar_usuarios(db)

# DELETE
@router.delete("/usuarios/{email}")
def remover_usuario(email: str, db: Session = Depends(get_db)):
    user = deletar_usuario(db, email)
    if not user:
        return {"erro": "Usuario não encontrado"}
    return {"mensagem": "Usuário deletado"}

# CONSULTAR
@router.get("/usuarios/{email}")
def consultar(email: str, db: Session = Depends(get_db)):
    user = buscar_usuario(db, email)
    if not user:
        return {"Erro":"Usuario não encontrado"}
    return {"mensagem":"Usuario encontrado"}
