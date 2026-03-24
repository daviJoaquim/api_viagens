from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tipo_combustivel import TipoCombustivelModel
from app.schemas.tipo_combustivel import TipoCombustivelSchema, TipoCombustivelResponse

tipo_combustivel = APIRouter(prefix="/tipo_combustivel",tags=["Tipo Combustível"])

@tipo_combustivel.post("/", response_model=TipoCombustivelSchema)
async def criar_tipo_combustivel(dados: TipoCombustivelSchema, db: Session = Depends(get_db)):
    criar_tipo_combustivel = TipoCombustivelModel(**dados.model_dump())
    db.add(criar_tipo_combustivel)
    db.commit()
    db.refresh(criar_tipo_combustivel)
    return criar_tipo_combustivel

@tipo_combustivel.get("/")
async def listar_tipo_combustivel(db: Session = Depends(get_db)):
    return db.query(TipoCombustivelModel).all()

@tipo_combustivel.get("/{id}")
async def buscar_tipo_combustivel(id_tipo_combustivel: int, db: Session = Depends(get_db)):
    tipo_combustivel = db.query(TipoCombustivelModel).filter(TipoCombustivelModel.id_tipo_combustivel == id_tipo_combustivel).first()
    if not tipo_combustivel:
        raise HTTPException(status_code=404, detail="Tipo Combustível não encontrado")
    return tipo_combustivel

@tipo_combustivel.put("/{id}")
async def atualizar_tipo_combustivel(id_tipo_combustivel: int, dados: TipoCombustivelResponse, db: Session = Depends(get_db)):
    tipo_combustivel = db.query(TipoCombustivelModel).filter(TipoCombustivelModel.id_tipo_combustivel == id_tipo_combustivel).first()
    if not tipo_combustivel:
        raise HTTPException(status_code=404, detail="Tipo Combustível não encontrado")
    
    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(tipo_combustivel, chave, valor)
    
    db.commit()
    db.refresh(tipo_combustivel)
    return tipo_combustivel

@tipo_combustivel.delete("/{id}")
async def apagar_tipo_combustivel(id_tipo_combustivel: int, db: Session = Depends(get_db)):
    tipo_combustivel = db.query(TipoCombustivelModel).filter(TipoCombustivelModel.id_tipo_combustivel == id_tipo_combustivel).first()
    if not tipo_combustivel:
        raise HTTPException(status_code=404, detail="Tipo Combustível não encontrado")
    
    db.delete(tipo_combustivel)
    db.commit()
    return {"message": "Tipo Combustível removida com sucesso"}