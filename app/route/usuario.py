from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import UsuarioModel
from app.schemas.usuario import UsuarioSchema, UsuarioResponse

usuario = APIRouter(prefix="/usuario",tags=["Usuário"])

@usuario.post("/", response_model=UsuarioSchema)
async def criar_usuario(dados: UsuarioSchema, db: Session = Depends(get_db)):
    criar_usuario = UsuarioModel(**dados.model_dump())
    db.add(criar_usuario)
    db.commit()
    db.refresh(criar_usuario)
    return criar_usuario

@usuario.get("/")
async def listar_usuario(db: Session = Depends(get_db)):
    return db.query(UsuarioModel).all()

@usuario.get("/{id}")
async def buscar_avaliacao(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

@usuario.put("/{id}")
async def atualizar_usuario(id_avaliacao: int, dados: UsuarioResponse, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id == id_avaliacao).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(usuario, chave, valor)
    
    db.commit()
    db.refresh(usuario)
    return usuario

@usuario.delete("/{id}")
async def apagar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id == id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrada")
    
    db.delete(usuario)
    db.commit()
    return {"message": "Usuário removido com sucesso"}