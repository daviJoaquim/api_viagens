from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.avaliacao import AvaliacaoModel
from app.schemas.avaliacao import AvaliacaoSchema, AvaliacaoResponse

avaliacao = APIRouter(prefix="/avaliação", tags=["Avaliação"])

@avaliacao.post("/", response_model=AvaliacaoSchema)
async def criar_avaliacao(dados: AvaliacaoSchema, db: Session = Depends(get_db)):
    criar_avaliacao = AvaliacaoModel(**dados.model_dump())
    db.add(criar_avaliacao)
    db.commit()
    db.refresh(criar_avaliacao)
    return criar_avaliacao

@avaliacao.get("/")
async def listar_avaliacoes(db: Session = Depends(get_db)):
    return db.query(AvaliacaoModel).all()

@avaliacao.get("/{id}")
async def buscar_avaliacao(id_avaliacao: int, db: Session = Depends(get_db)):
    res = db.query(AvaliacaoModel).filter(AvaliacaoModel.id_avaliacao == id_avaliacao).first()
    if not res:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    return res

@avaliacao.put("/{id}")
async def atualizar_avaliacao(id_avaliacao: int, dados: AvaliacaoResponse, db: Session = Depends(get_db)):
    item_db = db.query(AvaliacaoModel).filter(AvaliacaoModel.id_avaliacao == id_avaliacao).first()
    if not item_db:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    
    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(item_db, chave, valor)
    
    db.commit()
    db.refresh(item_db)
    return item_db

@avaliacao.delete("/{id}")
async def apagar_avaliacao(id_avaliacao: int, db: Session = Depends(get_db)):
    item_db = db.query(AvaliacaoModel).filter(AvaliacaoModel.id_avaliacao == id_avaliacao).first()
    if not item_db:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    
    db.delete(item_db)
    db.commit()
    return {"message": "Avaliação removida com sucesso"}