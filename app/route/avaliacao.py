from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.avaliacao import AvaliacaoModel
from app.schemas.avaliacao import AvaliacaoResponse, AvaliacaoSchema

viagens = APIRouter(prefix="/avaliacao", tags=["avaliacao"])

@viagens.post("/", response_model= AvaliacaoResponse)
async def criar_avaliacao(dados: AvaliacaoSchema, db: Session = Depends(get_db)):

    criar_avaliacao = AvaliacaoModel(**dados.model_dump())
    db.add(criar_avaliacao)
    db.commit()
    db.refresh(criar_avaliacao)
    return criar_avaliacao

@viagens.get("/", response_model=list[AvaliacaoResponse])
async def listar_avaliacao(db:Session = Depends(get_db)):
    return db.query(AvaliacaoModel).all()

@viagens.get("/{id}", response_model=AvaliacaoResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    avaliacao = db.query(AvaliacaoModel).filter(AvaliacaoModel.id_avaliacao == id).first()
    if not avaliacao:
        raise HTTPException(404, "Não encontrado")
    return avaliacao

@viagens.put("/{id}", response_model=AvaliacaoResponse)
async def atualizar_avaliacao(id: int, dados: AvaliacaoSchema, db: Session = Depends(get_db)):
   avaliacao = db.query(AvaliacaoModel).filter(AvaliacaoModel.id == id).first()

   if not avaliacao: 
       raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Avaliacão com ID {id} não encontrada"
        )
   
   for campo, valor in dados.model_dump().items():
       setattr(avaliacao, campo, valor)

   db.commit()
   db.refresh(avaliacao)

   return avaliacao

@viagens.delete("/{id}")
async def deletar_avaliacao(id: int, db:Session= Depends(get_db)):
    avaliacao = db.query(AvaliacaoModel).filter(AvaliacaoModel.id == id).first()

    if not avaliacao:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"O avaliacão com ID {id} não foi encontrada"
        )

        
    db.delete(avaliacao)
    db.commit()
    return("Deletado com sucesso!")


