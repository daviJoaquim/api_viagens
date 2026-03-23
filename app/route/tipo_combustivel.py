from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.tipo_combustivel import TipoCombustivelModel
from app.schemas.tipo_combustivel import TipoCombustivelResponse, TipoCombustivelSchema

viagens = APIRouter(prefix="/tipo_combustivel", tags=["tipo_combustivel"])

@viagens.post("/", response_model= TipoCombustivelResponse)
async def criar_tipo_combustivel(dados: TipoCombustivelSchema, db: Session = Depends(get_db)):

    criar_tipo_combustivel = TipoCombustivelModel(**dados.model_dump())
    db.add(criar_tipo_combustivel)
    db.commit()
    db.refresh(criar_tipo_combustivel)
    return criar_tipo_combustivel

@viagens.get("/", response_model=list[TipoCombustivelResponse])
async def listar_tipo_combustivel(db:Session = Depends(get_db)):
    return db.query(TipoCombustivelModel).all()

@viagens.get("/{id}", response_model=TipoCombustivelResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    tipo_combustivel = db.query(TipoCombustivelModel).filter(TipoCombustivelModel.id_tipo_combustivel == id).first()
    if not tipo_combustivel:
        raise HTTPException(404, "Não encontrado")
    return tipo_combustivel

@viagens.put("/{id}", response_model=TipoCombustivelResponse)
async def atualizar_tipo_combustivel(id: int, dados: TipoCombustivelSchema, db: Session = Depends(get_db)):
   tipo_combustivel = db.query(TipoCombustivelModel).filter(TipoCombustivelModel.id_tipo_combustivel == id).first()

   if not tipo_combustivel: 
       raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Tipo combustível com ID {id} não encontrada"
        )
   
   for campo, valor in dados.model_dump().items():
       setattr(tipo_combustivel, campo, valor)

   db.commit()
   db.refresh(tipo_combustivel)

   return tipo_combustivel

@viagens.delete("/{id}")
async def deletar_tipo_combustivel(id: int, db:Session= Depends(get_db)):
    tipo_combustivel = db.query(TipoCombustivelModel).filter(TipoCombustivelModel.id_tipo_combustivel == id).first()

    if not tipo_combustivel:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"O tipo combustível com ID {id} não foi encontrada"
        )

        
    db.delete(tipo_combustivel)
    db.commit()
    return("Deletado com sucesso!")


