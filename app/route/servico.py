from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.servico import ServicoModel
from app.schemas.servico import ServicoResponse, ServicoSchema

viagens = APIRouter(prefix="/servico", tags=["servico"])

@viagens.post("/", response_model= ServicoResponse)
async def criar_servico(dados: ServicoSchema, db: Session = Depends(get_db)):

    criar_servico = ServicoModel(**dados.model_dump())
    db.add(criar_servico)
    db.commit() 
    db.refresh(criar_servico)
    return criar_servico

@viagens.get("/", response_model=list[ServicoResponse])
async def listar_servico(db:Session = Depends(get_db)):
    return db.query(ServicoModel).all()

@viagens.get("/{id}", response_model=ServicoResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    servico = db.query(ServicoModel).filter(ServicoModel.id_servico == id).first()
    if not servico:
        raise HTTPException(404, "Não encontrado")
    return servico

@viagens.put("/{id}", response_model=ServicoResponse)
async def atualizar_servico(id: int, dados: ServicoSchema, db: Session = Depends(get_db)):
   servico = db.query(ServicoModel).filter(ServicoModel.id == id).first()

   if not servico: 
       raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Serviço com ID {id} não encontrada"
        )
   
   for campo, valor in dados.model_dump().items():
       setattr(servico, campo, valor)

   db.commit()
   db.refresh(servico)

   return servico

@viagens.delete("/{id}")
async def deletar_servico(id: int, db:Session= Depends(get_db)):
    servico = db.query(ServicoModel).filter(ServicoModel.id == id).first()

    if not servico:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"O serviço com ID {id} não foi encontrada"
        )

        
    db.delete(servico)
    db.commit()
    return("Deletado com sucesso!")


