from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.passageiro import PassageiroModel
from app.schemas.passageiro import PassageiroResponse, PassageiroSchema

viagens = APIRouter(prefix="/passageiro", tags=["passageiro"])

@viagens.post("/", response_model= PassageiroResponse)
async def criar_passageiro(dados: PassageiroSchema, db: Session = Depends(get_db)):

    criar_passageiro = PassageiroModel(**dados.model_dump())
    db.add(criar_passageiro)
    db.commit() 
    db.refresh(criar_passageiro)
    return criar_passageiro

@viagens.get("/", response_model=list[PassageiroResponse])
async def listar_passageiro(db:Session = Depends(get_db)):
    return db.query(PassageiroModel).all()

@viagens.get("/{id}", response_model=PassageiroResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    passageiro = db.query(PassageiroModel).filter(PassageiroModel.id_passageiro == id).first()
    if not passageiro:
        raise HTTPException(404, "Não encontrado")
    return passageiro

@viagens.put("/{id}", response_model=PassageiroResponse)
async def atualizar_passageiro(id: int, dados: PassageiroSchema, db: Session = Depends(get_db)):
   passageiro = db.query(PassageiroModel).filter(PassageiroModel.id == id).first()

   if not passageiro: 
       raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Passageiro com ID {id} não encontrada"
        )
   
   for campo, valor in dados.model_dump().items():
       setattr(passageiro, campo, valor)

   db.commit()
   db.refresh(passageiro)

   return passageiro

@viagens.delete("/{id}")
async def deletar_passageiro(id: int, db:Session= Depends(get_db)):
    passageiro = db.query(PassageiroModel).filter(PassageiroModel.id == id).first()

    if not passageiro:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"O passageiro com ID {id} não foi encontrada"
        )

        
    db.delete(passageiro)
    db.commit()
    return("Deletado com sucesso!")


