from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.pagamentos import PagamentosModel
from app.schemas.pagamentos import PagamentoResponse, PagamentoSchema

viagens = APIRouter(prefix="/pagamento", tags=["pagamento"])

@viagens.post("/", response_model= PagamentoResponse)
async def criar_pagamento(dados: PagamentoSchema, db: Session = Depends(get_db)):

    criar_pagamento = PagamentosModel(**dados.model_dump())
    db.add(criar_pagamento)
    db.commit() 
    db.refresh(criar_pagamento)
    return criar_pagamento

@viagens.get("/", response_model=list[PagamentoResponse])
async def listar_pagamento(db:Session = Depends(get_db)):
    return db.query(PagamentosModel).all()

@viagens.get("/{id}", response_model=PagamentoResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    pagamento = db.query(PagamentosModel).filter(PagamentosModel.id_pagamento == id).first()
    if not pagamento:
        raise HTTPException(404, "Não encontrado")
    return pagamento

@viagens.put("/{id}", response_model=PagamentoResponse)
async def atualizar_pagamento(id: int, dados: PagamentoSchema, db: Session = Depends(get_db)):
   pagamento = db.query(PagamentosModel).filter(PagamentosModel.id == id).first()

   if not pagamento: 
       raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Pagamento com ID {id} não encontrada"
        )
   
   for campo, valor in dados.model_dump().items():
       setattr(pagamento, campo, valor)

   db.commit()
   db.refresh(pagamento)

   return pagamento

@viagens.delete("/{id}")
async def deletar_pagamento(id: int, db:Session= Depends(get_db)):
    pagamento = db.query(PagamentosModel).filter(PagamentosModel.id == id).first()

    if not pagamento:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"O pagamento com ID {id} não foi encontrada"
        )

        
    db.delete(pagamento)
    db.commit()
    return("Deletado com sucesso!")


