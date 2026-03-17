from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.classe import ClasseModel
from app.schemas.classe import ClasseResponse, ClasseSchema

viagens = APIRouter(prefix="/classe", tags=["classe"])

@viagens.post("/", response_model= ClasseResponse)
async def criar_classe(dados: ClasseSchema, db: Session = Depends(get_db)):

    criar_classe = ClasseModel(**dados.model_dump())
    db.add(criar_classe)
    db.commit()
    db.refresh(criar_classe)
    return criar_classe

@viagens.get("/", response_model=list[ClasseResponse])
async def listar_classe(db:Session = Depends(get_db)):
    return db.query(ClasseModel).all()

@viagens.get("/{id}", response_model=ClasseResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    classe = db.query(ClasseModel).filter(ClasseModel.id_classe == id).first()
    if not classe:
        raise HTTPException(404, "Não encontrado")
    return classe

@viagens.put("/{id}", response_model=ClasseResponse)
async def atualizar_classe(id: int, dados: ClasseSchema, db: Session = Depends(get_db)):
   classe = db.query(ClasseModel).filter(ClasseModel.id == id).first()

   if not classe: 
       raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Avaliacão com ID {id} não encontrada"
        )
   
   for campo, valor in dados.model_dump().items():
       setattr(classe, campo, valor)

   db.commit()
   db.refresh(classe)

   return classe

@viagens.delete("/{id}")
async def deletar_classe(id: int, db:Session= Depends(get_db)):
    classe = db.query(ClasseModel).filter(ClasseModel.id == id).first()

    if not classe:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"O avaliacão com ID {id} não foi encontrada"
        )

        
    db.delete(classe)
    db.commit()
    return("Deletado com sucesso!")


