from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.servico import ServicoModel
from app.schemas.servico import ServicoSchema, ServicoResponse

servico = APIRouter(prefix="/servico",tags=["Serviço"])

@servico.post("/", response_model=ServicoSchema)
async def criar_servico(dados: ServicoSchema, db: Session = Depends(get_db)):
    criar_servico = ServicoModel(**dados.model_dump())
    db.add(criar_servico)
    db.commit()
    db.refresh(criar_servico)
    return criar_servico

@servico.get("/")
async def listar_servico(db: Session = Depends(get_db)):
    return db.query(ServicoModel).all()

@servico.get("/{id}")
async def buscar_servico(id_servico: int, db: Session = Depends(get_db)):
    servico = db.query(ServicoModel).filter(ServicoModel.id_servico == id_servico).first()
    if not servico:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
    return servico

@servico.put("/{id}")
async def atualizar_servico(id_servico: int, dados: ServicoResponse, db: Session = Depends(get_db)):
    servico = db.query(ServicoModel).filter(ServicoModel.id_servico == id_servico).first()
    if not servico:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
    
    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(servico, chave, valor)
    
    db.commit()
    db.refresh(servico)
    return servico

@servico.delete("/{id}")
async def apagar_servico(id_servico: int, db: Session = Depends(get_db)):
    servico = db.query(ServicoModel).filter(ServicoModel.id_servico == id_servico).first()
    if not servico:
        raise HTTPException(status_code=404, detail="Serviço não encontrado")
    
    db.delete(servico)
    db.commit()
    return {"message": "Serviço removido com sucesso"}