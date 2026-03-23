from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.corrida import CorridaModel
from app.schemas.corrida import CorridaResponse, CorridaSchema

viagens = APIRouter(prefix="/corrida", tags=["corrida"])

@viagens.post("/", response_model= CorridaResponse)
async def criar_corrida(dados: CorridaSchema, db: Session = Depends(get_db)):

    criar_corrida = CorridaModel(**dados.model_dump())
    db.add(criar_corrida)
    db.commit()
    db.refresh(criar_corrida)
    return criar_corrida

@viagens.get("/", response_model=list[CorridaResponse])
async def listar_corrida(db:Session = Depends(get_db)):
    return db.query(CorridaModel).all()

@viagens.get("/{id}", response_model=CorridaResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    corrida = db.query(CorridaModel).filter(CorridaModel.id_corrida == id).first()
    if not corrida:
        raise HTTPException(404, "Não encontrado")
    return corrida

@viagens.put("/{id}", response_model=CorridaResponse)
async def atualizar_corrida(id: int, dados: CorridaSchema, db: Session = Depends(get_db)):
   corrida = db.query(CorridaModel).filter(CorridaModel.id_corrida == id).first()

   if not corrida: 
       raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Corrida com ID {id} não encontrada"
        )
   
   for campo, valor in dados.model_dump().items():
       setattr(corrida, campo, valor)

   db.commit()
   db.refresh(corrida)

   return corrida

@viagens.delete("/{id}")
async def deletar_corrida(id: int, db:Session= Depends(get_db)):
    corrida = db.query(CorridaModel).filter(CorridaModel.id_corrida == id).first()

    if not corrida:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"O corrida com ID {id} não foi encontrada"
        )

        
    db.delete(corrida)
    db.commit()
    return("Deletado com sucesso!")


