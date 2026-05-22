from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.auth.security import hash_password
from app.auth.security import verify_password
from app.auth.jwt import create_access_token

# CREATE

def criar_usuario(db: Session, nome: str, email: str, senha: str):
    hashed_password = hash_password(senha)

    user = Usuario(
        nome=nome,
        email=email,
        senha=hashed_password  # 🔥 agora é hash
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login(db, email: str, senha: str):
    user = db.query(Usuario).filter(Usuario.email == email).first()

    if not user:
        return None

    if not verify_password(senha, user.senha):
        return None

    token = create_access_token({"sub": user.email})
    return token


# READ
def listar_usuarios(db: Session):
    return db.query(Usuario).all()

def buscar_usuario(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()


# DELETE
def deletar_usuario(db:Session, email: str):
    user = db.query(Usuario).filter(Usuario.email == email).first()

    if not user:
        return None
    
    db.delete(user)
    db.commit()

    print(f"💾 Apagado {user}")
    return user

