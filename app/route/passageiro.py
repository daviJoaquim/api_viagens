from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.passageiro import PassageiroModel
from app.schemas.passageiro import PassageiroSchema, PassageiroResponse

passageiro = APIRouter(prefix="/passageiro",tags=["Passageiro"])

@passageiro.post("/", response_model=PassageiroSchema)
async def criar_passageiro(dados: PassageiroSchema, db: Session = Depends(get_db)):
    criar_passageiro = PassageiroModel(**dados.model_dump())
    db.add(criar_passageiro)
    db.commit()
    db.refresh(criar_passageiro)
    return criar_passageiro

@passageiro.get("/")
async def listar_passageiro(db: Session = Depends(get_db)):
    return db.query(PassageiroModel).all()

@passageiro.get("/{id}")
async def buscar_passageiro(id_passageiro: int, db: Session = Depends(get_db)):
    passageiro = db.query(PassageiroModel).filter(PassageiroModel.id_passageiro == id_passageiro).first()
    if not passageiro:
        raise HTTPException(status_code=404, detail="Passageiro não encontrado")
    return passageiro

@passageiro.put("/{id}")
async def atualizar_passageiro(id_passageiro: int, dados: PassageiroResponse, db: Session = Depends(get_db)):
    passageiro = db.query(PassageiroModel).filter(PassageiroModel.id_passageiro == id_passageiro).first()
    if not passageiro:
        raise HTTPException(status_code=404, detail="Passageiro não encontrado")
    
    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(passageiro, chave, valor)
    
    db.commit()
    db.refresh(passageiro)
    return passageiro

@passageiro.delete("/{id}")
async def apagar_passageiro(id_passageiro: int, db: Session = Depends(get_db)):
    passageiro = db.query(PassageiroModel).filter(PassageiroModel.id_passageiro == id_passageiro).first()
    if not passageiro:
        raise HTTPException(status_code=404, detail="Passageiro não encontrado")
    
    db.delete(passageiro)
    db.commit()
    return {"message": "Passageiro removida com sucesso"}