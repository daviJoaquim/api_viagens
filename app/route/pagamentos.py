from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.pagamentos import PagamentosModel
from app.schemas.pagamentos import PagamentoSchema, PagamentoResponse

pagamentos = APIRouter(prefix="/pagamentos", tags=["Pagamentos"])

@pagamentos.post("/", response_model=PagamentoSchema)
async def criar_pagamentos(dados: PagamentoSchema, db: Session = Depends(get_db)):
    criar_pagamentos = PagamentosModel(**dados.model_dump())
    db.add(criar_pagamentos)
    db.commit()
    db.refresh(criar_pagamentos)
    return criar_pagamentos

@pagamentos.get("/")
async def listar_pagamentos(db: Session = Depends(get_db)):
    return db.query(PagamentosModel).all()

@pagamentos.get("/{id}")
async def buscar_pagamentos(id_pagamentos: int, db: Session = Depends(get_db)):
    pagamentos = db.query(PagamentosModel).filter(PagamentosModel.id_pagamento == id_pagamentos).first()
    if not pagamentos:
        raise HTTPException(status_code=404, detail="Pagamentos não encontrados")
    return pagamentos

@pagamentos.put("/{id}")
async def atualizar_pagamentos(id_pagamentos: int, dados: PagamentoResponse, db: Session = Depends(get_db)):
    pagamentos = db.query(PagamentosModel).filter(PagamentosModel.id_pagamento == id_pagamentos).first()
    if not pagamentos:
        raise HTTPException(status_code=404, detail="Pagamentos não encontrados")
    
    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(pagamentos, chave, valor)
    
    db.commit()
    db.refresh(pagamentos)
    return pagamentos

@pagamentos.delete("/{id}")
async def apagar_avaliacao(id_pagamentos: int, db: Session = Depends(get_db)):
    pagamentos = db.query(PagamentosModel).filter(PagamentosModel.id_pagamento == id_pagamentos).first()
    if not pagamentos:
        raise HTTPException(status_code=404, detail="Pagamentos não encontrados")
    
    db.delete(pagamentos)
    db.commit()
    return {"message": "Pagamentos removido com sucesso"}