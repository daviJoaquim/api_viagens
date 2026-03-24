from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.metodo_pagamento import MetodoPagamentoModel
from app.schemas.metodo_pagamento import MetodoPagamentoSchema, MetodoPagamentoResponse

metodo_pagamento = APIRouter(prefix="/corrida",tags=["Método Pagamento"])

@metodo_pagamento.post("/", response_model=MetodoPagamentoSchema)
async def criar_metodo_pagamento(dados: MetodoPagamentoSchema, db: Session = Depends(get_db)):
    criar_metodo_pagamento = MetodoPagamentoModel(**dados.model_dump())
    db.add(criar_metodo_pagamento)
    db.commit()
    db.refresh(criar_metodo_pagamento)
    return criar_metodo_pagamento

@metodo_pagamento.get("/")
async def listar_metodo_pagamento(db: Session = Depends(get_db)):
    return db.query(MetodoPagamentoModel).all()

@metodo_pagamento.get("/{id}")
async def buscar_metodo_pagamento(id_metodo_pagamento: int, db: Session = Depends(get_db)):
    metodo_pagamento = db.query(MetodoPagamentoModel).filter(MetodoPagamentoModel.id_metodo_pagamento == id_metodo_pagamento).first()
    if not metodo_pagamento:
        raise HTTPException(status_code=404, detail="Método Pagamento não encontrada")
    return metodo_pagamento

@metodo_pagamento.put("/{id}")
async def atualizar_metodo_pagamento(id_metodo_pagamento: int, dados: MetodoPagamentoResponse, db: Session = Depends(get_db)):
    metodo_pagamento = db.query(MetodoPagamentoModel).filter(MetodoPagamentoModel.id_metodo_pagamento == id_metodo_pagamento).first()
    if not metodo_pagamento:
        raise HTTPException(status_code=404, detail="Método Pagamento não encontrada")
    
    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(metodo_pagamento, chave, valor)
    
    db.commit()
    db.refresh(metodo_pagamento)
    return metodo_pagamento

@metodo_pagamento.delete("/{id}")
async def apagar_avaliacao(id_metodo_pagamento: int, db: Session = Depends(get_db)):
    metodo_pagamento = db.query(MetodoPagamentoModel).filter(MetodoPagamentoModel.id_metodo_pagamento == id_metodo_pagamento).first()
    if not metodo_pagamento:
        raise HTTPException(status_code=404, detail="Método Pagamento não encontrada")
    
    db.delete(metodo_pagamento)
    db.commit()
    return {"message": "Avaliação removida com sucesso"}