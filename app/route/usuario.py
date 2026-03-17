from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import UsuarioModel
from app.schemas.usuario import UsuarioCreate, UsuarioResponse

viagens = APIRouter(prefix="/usuario", tags=["usuario"])

@viagens.post("/", response_model= UsuarioResponse)
async def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):

    criar_usuario = UsuarioModel(
        nome = usuario.nome,
        cpf = usuario.cpf,
        data_nascimento = usuario.data_nascimento,
        email = usuario.email,
        usuario = usuario.usuario,
        senha = usuario.senha
    )
    db.add(criar_usuario)
    db.commit()
    db.refresh(criar_usuario)
    return criar_usuario

@viagens.get("/", response_model=list[UsuarioResponse])
async def listar_usuarios(db:Session = Depends(get_db)):
    return db.query(UsuarioModel).all()

@viagens.put("/{id}", response_model=UsuarioResponse)
async def atualizar_usuarios(id: int, dados: UsuarioCreate, db: Session = Depends(get_db)):
   usuario = db.query(UsuarioModel).filter(UsuarioModel.id == id).first()

   if not usuario: 
       raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Usuário com ID {id} não encontrada"
        )
   
   for campo, valor in dados.model_dump().items():
       setattr(usuario, campo, valor)

   db.commit()
   db.refresh(usuario)

   return usuario

@viagens.delete("{id}")
async def deletar_series(id: int, db:Session= Depends(get_db)):
    
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id == id).first()

    if not id:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"O usuário com ID {id} não foi encontrada"
        )

        
    db.delete(usuario)
    db.commit()
    return("Deletado com sucesso!")


