from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.motorista import MotoristaModel
from app.schemas.motorista import MotoristaSchema, MotoristaResponse

motorista = APIRouter(prefix="/motorista",tags=["Motorista"])

@motorista.post("/", response_model=MotoristaSchema)
async def criar_motorista(dados: MotoristaSchema, db: Session = Depends(get_db)):
    criar_motorista = MotoristaModel(**dados.model_dump())
    db.add(criar_motorista)
    db.commit()
    db.refresh(criar_motorista)
    return criar_motorista

@motorista.get("/")
async def listar_motorista(db: Session = Depends(get_db)):
    return db.query(MotoristaModel).all()

@motorista.get("/{id}")
async def buscar_motorista(id_motorista: int, db: Session = Depends(get_db)):
    motorista = db.query(MotoristaModel).filter(MotoristaModel.id_motorista == id_motorista).first()
    if not motorista:
        raise HTTPException(status_code=404, detail="Motorista não encontrado")
    return motorista

@motorista.put("/{id}")
async def atualizar_motorista(id_motorista: int, dados: MotoristaResponse, db: Session = Depends(get_db)):
    motorista = db.query(MotoristaModel).filter(MotoristaModel.id_motorista == id_motorista).first()
    if not motorista:
        raise HTTPException(status_code=404, detail="Motorista não encontrado")
    
    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(motorista, chave, valor)
    
    db.commit()
    db.refresh(motorista)
    return motorista

@motorista.delete("/{id}")
async def apagar_motorista(id_motorista: int, db: Session = Depends(get_db)):
    motorista = db.query(MotoristaModel).filter(MotoristaModel.id_motorista == id_motorista).first()
    if not motorista:
        raise HTTPException(status_code=404, detail="Motorista não encontrado")
    
    db.delete(motorista)
    db.commit()
    return {"message": "Motorista removido com sucesso"}