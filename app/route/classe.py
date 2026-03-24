from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.classe import ClasseModel
from app.schemas.classe import ClasseSchema, ClasseResponse

classe = APIRouter(prefix="/classe",tags=["Classe"])

@classe.post("/", response_model= ClasseSchema)
async def criar_classe(dados: ClasseSchema, db: Session = Depends(get_db)):
    criar_classe = ClasseModel(**dados.model_dump())
    db.add(criar_classe)
    db.commit()
    db.refresh(criar_classe)
    return criar_classe

@classe.get("/")
async def listar_classe(db: Session = Depends(get_db)):
    return db.query(ClasseModel).all()

@classe.get("/{id}")
async def buscar_classe(id_classe: int, db: Session = Depends(get_db)):
    res = db.query(ClasseModel).filter(ClasseModel.id_classe == id_classe).first()
    if not res:
        raise HTTPException(status_code=404, detail="Classe não encontrada")
    return res

@classe.put("/{id}")
async def atualizar_classe(id_classe: int, dados: ClasseResponse, db: Session = Depends(get_db)):
    classe = db.query(ClasseModel).filter(ClasseModel.id_classe == id_classe).first()
    if not classe:
        raise HTTPException(status_code=404, detail="Classe não encontrada")
    
    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(classe, chave, valor)
    
    db.commit()
    db.refresh(classe)
    return classe

@classe.delete("/{id}")
async def apagar_classe(id_classe: int, db: Session = Depends(get_db)):
    classe = db.query(ClasseModel).filter(ClasseModel.id_classe == id_classe).first()
    if not classe:
        raise HTTPException(status_code=404, detail="Classe não encontrada")
    
    db.delete(classe)
    db.commit()
    return {"message": "Classe removida com sucesso"}