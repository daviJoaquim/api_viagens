from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.modelo_veiculo import ModeloVeiculoModel
from app.schemas.modelo_veiculo import ModeloVeiculoResponse, ModeloVeiculoSchema

viagens = APIRouter(prefix="/modelo_veiculo", tags=["modelo_veiculo"])

@viagens.post("/", response_model= ModeloVeiculoResponse)
async def criar_modelo_veiculo(dados: ModeloVeiculoSchema, db: Session = Depends(get_db)):

    criar_modelo_veiculo = ModeloVeiculoModel(**dados.model_dump())
    db.add(criar_modelo_veiculo)
    db.commit()
    db.refresh(criar_modelo_veiculo)
    return criar_modelo_veiculo

@viagens.get("/", response_model=list[ModeloVeiculoResponse])
async def listar_modelo_veiculo(db:Session = Depends(get_db)):
    return db.query(ModeloVeiculoModel).all()

@viagens.get("/{id}", response_model=ModeloVeiculoResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    modelo_veiculo = db.query(ModeloVeiculoModel).filter(ModeloVeiculoModel.id_modelo_veiculo == id).first()
    if not modelo_veiculo:
        raise HTTPException(404, "Não encontrado")
    return modelo_veiculo

@viagens.put("/{id}", response_model= ModeloVeiculoResponse)
async def atualizar_modelo_veiculo(id: int, dados: ModeloVeiculoSchema, db: Session = Depends(get_db)):
   modelo_veiculo = db.query(ModeloVeiculoModel).filter(ModeloVeiculoModel.id_modelo_veiculo == id).first()

   if not modelo_veiculo: 
       raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Modelo veículo com ID {id} não encontrada"
        )
   
   for campo, valor in dados.model_dump().items():
       setattr(modelo_veiculo, campo, valor)

   db.commit()
   db.refresh(modelo_veiculo)

   return modelo_veiculo

@viagens.delete("/{id}")
async def deletar_modelo_veiculo(id: int, db:Session= Depends(get_db)):
    modelo_veiculo = db.query(ModeloVeiculoModel).filter(ModeloVeiculoModel.id_modelo_veiculo == id).first()

    if not modelo_veiculo:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"O modelo veículo com ID {id} não foi encontrada"
        )

        
    db.delete(modelo_veiculo)
    db.commit()
    return("Deletado com sucesso!")


