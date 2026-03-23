from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.metodo_pagamento import MetodoPagamentoModel
from app.schemas.metodo_pagamento import MetodoPagamentoResponse, MetodoPagamentoSchema

viagens = APIRouter(prefix="/metodo_pagamento", tags=["metodo_pagamento"])

@viagens.post("/", response_model= MetodoPagamentoResponse)
async def criar_metodo_pagamento(dados: MetodoPagamentoSchema, db: Session = Depends(get_db)):

    criar_metodo_pagamento = MetodoPagamentoModel(**dados.model_dump())
    db.add(criar_metodo_pagamento)
    db.commit()
    db.refresh(criar_metodo_pagamento)
    return criar_metodo_pagamento

@viagens.get("/", response_model=list[MetodoPagamentoResponse])
async def listar_metodo_pagamento(db:Session = Depends(get_db)):
    return db.query(MetodoPagamentoModel).all()

@viagens.get("/{id}", response_model=MetodoPagamentoResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    metodo_pagamento = db.query(MetodoPagamentoModel).filter(MetodoPagamentoModel.id_metodo_pagamento == id).first()
    if not metodo_pagamento:
        raise HTTPException(404, "Não encontrado")
    return metodo_pagamento

@viagens.put("/{id}", response_model=MetodoPagamentoResponse)
async def atualizar_metodo_pagamento(id: int, dados: MetodoPagamentoSchema, db: Session = Depends(get_db)):
   metodo_pagamento = db.query(MetodoPagamentoModel).filter(MetodoPagamentoModel.id_metodo_pagamento == id).first()

   if not metodo_pagamento: 
       raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Corrida com ID {id} não encontrada"
        )
   
   for campo, valor in dados.model_dump().items():
       setattr(metodo_pagamento, campo, valor)

   db.commit()
   db.refresh(metodo_pagamento)

   return metodo_pagamento

@viagens.delete("/{id}")
async def deletar_metodo_pagamento(id: int, db:Session= Depends(get_db)):
    metodo_pagamento = db.query(MetodoPagamentoModel).filter(MetodoPagamentoModel.id_metodo_pagamento == id).first()

    if not metodo_pagamento:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"O metodo pagamento com ID {id} não foi encontrada"
        )

        
    db.delete(metodo_pagamento)
    db.commit()
    return("Deletado com sucesso!")


