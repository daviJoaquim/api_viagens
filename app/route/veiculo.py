from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.veiculo import VeiculoModel
from app.schemas.veiculo import VeiculoResponse, VeiculoSchema

viagens = APIRouter(prefix="/veiculo", tags=["veiculo"])

@viagens.post("/", response_model= VeiculoResponse)
async def criar_veiculo(dados: VeiculoSchema, db: Session = Depends(get_db)):

    criar_veiculo = VeiculoModel(**dados.model_dump())
    db.add(criar_veiculo)
    db.commit()
    db.refresh(criar_veiculo)
    return criar_veiculo

@viagens.get("/", response_model=list[VeiculoResponse])
async def listar_veiculo(db:Session = Depends(get_db)):
    return db.query(VeiculoModel).all()

@viagens.get("/{id}", response_model=VeiculoResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    veiculo = db.query(VeiculoModel).filter(VeiculoModel.id_veiculo == id).first()
    if not veiculo:
        raise HTTPException(404, "Não encontrado")
    return veiculo

@viagens.put("/{id}", response_model= VeiculoResponse)
async def atualizar_veiculo(id: int, dados: VeiculoSchema, db: Session = Depends(get_db)):
   veiculo = db.query(VeiculoModel).filter(VeiculoModel.id_veiculo == id).first()

   if not veiculo: 
       raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Veiculo com ID {id} não encontrada"
        )
   
   for campo, valor in dados.model_dump().items():
       setattr(veiculo, campo, valor)

   db.commit()
   db.refresh(veiculo)

   return veiculo

@viagens.delete("/{id}")
async def deletar_veiculo(id: int, db:Session= Depends(get_db)):
    veiculo = db.query(VeiculoModel).filter(VeiculoModel.id_veiculo == id).first()

    if not veiculo:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"O veiculo com ID {id} não foi encontrada"
        )

        
    db.delete(veiculo)
    db.commit()
    return("Deletado com sucesso!")


