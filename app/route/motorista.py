from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.motorista import MotoristaModel
from app.schemas.motorista import MotoristaResponse, MotoristaSchema

viagens = APIRouter(prefix="/motorista", tags=["motorista"])

@viagens.post("/", response_model= MotoristaResponse)
async def criar_motorista(dados: MotoristaSchema, db: Session = Depends(get_db)):

    criar_motorista = MotoristaModel(**dados.model_dump())
    db.add(criar_motorista)
    db.commit() 
    db.refresh(criar_motorista)
    return criar_motorista

@viagens.get("/", response_model=list[MotoristaResponse])
async def listar_motorista(db:Session = Depends(get_db)):
    return db.query(MotoristaModel).all()

@viagens.get("/{id}", response_model=MotoristaResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    motorista = db.query(MotoristaModel).filter(MotoristaModel.id_motorista == id).first()
    if not motorista:
        raise HTTPException(404, "Não encontrado")
    return motorista

@viagens.put("/{id}", response_model=MotoristaResponse)
async def atualizar_motorista(id: int, dados: MotoristaSchema, db: Session = Depends(get_db)):
   motorista = db.query(MotoristaModel).filter(MotoristaModel.id == id).first()

   if not motorista: 
       raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Motorista com ID {id} não encontrada"
        )
   
   for campo, valor in dados.model_dump().items():
       setattr(motorista, campo, valor)

   db.commit()
   db.refresh(motorista)

   return motorista

@viagens.delete("/{id}")
async def deletar_motorista(id: int, db:Session= Depends(get_db)):
    motorista = db.query(MotoristaModel).filter(MotoristaModel.id == id).first()

    if not motorista:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"O motorista com ID {id} não foi encontrada"
        )

        
    db.delete(motorista)
    db.commit()
    return("Deletado com sucesso!")


