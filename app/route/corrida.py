from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.corrida import CorridaModel
from app.schemas.corrida import CorridaSchema, CorridaResponse

corrida = APIRouter(prefix="/corrida", tags=["Corrida"])

@corrida.post("/", response_model=CorridaSchema)
async def criar_corrida(dados: CorridaSchema, db: Session = Depends(get_db)):
    criar_corrida = CorridaModel(**dados.model_dump())
    db.add(criar_corrida)
    db.commit()
    db.refresh(criar_corrida)
    return criar_corrida

@corrida.get("/")
async def listar_corrida(db: Session = Depends(get_db)):
    return db.query(CorridaModel).all()

@corrida.get("/{id}")
async def buscar_corrida(id_corrida: int, db: Session = Depends(get_db)):
    corrida = db.query(CorridaModel).filter(CorridaModel.id_corrida == id_corrida).first()
    if not corrida:
        raise HTTPException(status_code=404, detail="Corrida não encontrada")
    return corrida

@corrida.put("/{id}")
async def atualizar_corrida(id_corrida: int, dados: CorridaResponse, db: Session = Depends(get_db)):
    corrida = db.query(CorridaModel).filter(CorridaModel.id_corrida == id_corrida).first()
    if not corrida:
        raise HTTPException(status_code=404, detail="Corrida não encontrada")
    
    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(corrida, chave, valor)
    
    db.commit()
    db.refresh(corrida)
    return corrida

@corrida.delete("/{id}")
async def apagar_corrida(id_corrida: int, db: Session = Depends(get_db)):
    corrida = db.query(CorridaModel).filter(CorridaModel.id_corrida == id_corrida).first()
    if not corrida:
        raise HTTPException(status_code=404, detail="Corrida não encontrada")
    
    db.delete(corrida)
    db.commit()
    return {"message": "Corrida removida com sucesso"}