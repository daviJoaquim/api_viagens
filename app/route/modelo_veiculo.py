from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.modelo_veiculo import ModeloVeiculoModel
from app.schemas.modelo_veiculo import ModeloVeiculoSchema, ModeloVeiculoResponse

modelo_veiculo = APIRouter(prefix="/corrida",tags=["Modelo Veículo"])

@modelo_veiculo.post("/", response_model=ModeloVeiculoSchema)
async def criar_modelo_veiculo(dados: ModeloVeiculoSchema, db: Session = Depends(get_db)):
    criar_modelo_veiculo = ModeloVeiculoModel(**dados.model_dump())
    db.add(criar_modelo_veiculo)
    db.commit()
    db.refresh(criar_modelo_veiculo)
    return criar_modelo_veiculo

@modelo_veiculo.get("/")
async def listar_modelo_veiculo(db: Session = Depends(get_db)):
    return db.query(ModeloVeiculoModel).all()

@modelo_veiculo.get("/{id}")
async def buscar_modelo_veiculo(id_modelo_veiculo: int, db: Session = Depends(get_db)):
    modelo_veiculo = db.query(ModeloVeiculoModel).filter(ModeloVeiculoModel.id_modelo_veiculo == id_modelo_veiculo).first()
    if not modelo_veiculo:
        raise HTTPException(status_code=404, detail="Modelo Veículo não encontrada")
    return modelo_veiculo

@modelo_veiculo.put("/{id}")
async def atualizar_modelo_veiculo(id_modelo_veiculo: int, dados: ModeloVeiculoResponse, db: Session = Depends(get_db)):
    modelo_veiculo = db.query(ModeloVeiculoModel).filter(ModeloVeiculoModel.id_modelo_veiculo == id_modelo_veiculo).first()
    if not modelo_veiculo:
        raise HTTPException(status_code=404, detail="Modelo Veículo não encontrada")
    
    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(modelo_veiculo, chave, valor)
    
    db.commit()
    db.refresh(modelo_veiculo)
    return modelo_veiculo

@modelo_veiculo.delete("/{id}")
async def apagar_modelo_veiculo(id_modelo_veiculo: int, db: Session = Depends(get_db)):
    modelo_veiculo = db.query(ModeloVeiculoModel).filter(ModeloVeiculoModel.id_modelo_veiculo == id_modelo_veiculo).first()
    if not modelo_veiculo:
        raise HTTPException(status_code=404, detail="Modelo Veículo não encontrado")
    
    db.delete(modelo_veiculo)
    db.commit()
    return {"message": "Modelo Veículo removido com sucesso"}