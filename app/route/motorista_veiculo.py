from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.motorista_veiculo import MotoristaVeiculoModel
from app.schemas.motorista_veiculo import MotoristaVeiculoSchema, MotoristaVeiculoResponse

motorista_veiculo = APIRouter(prefix="/motorista_veiculo", tags=["Motorista Veículo"])

@motorista_veiculo.post("/", response_model=MotoristaVeiculoSchema)
async def criar_motorista_veiculo(dados: MotoristaVeiculoSchema, db: Session = Depends(get_db)):
    criar_motorista_veiculo = MotoristaVeiculoModel(**dados.model_dump())
    db.add(criar_motorista_veiculo)
    db.commit()
    db.refresh(criar_motorista_veiculo)
    return criar_motorista_veiculo

@motorista_veiculo.get("/")
async def listar_motorista_veiculo(db: Session = Depends(get_db)):
    return db.query(MotoristaVeiculoModel).all()

@motorista_veiculo.get("/{id}")
async def buscar_motorista_veiculo(id_motorista_veiculo: int, db: Session = Depends(get_db)):
    motorista_veiculo = db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id_motorista_veiculo == id_motorista_veiculo).first()
    if not motorista_veiculo:
        raise HTTPException(status_code=404, detail="Motorista Veículo não encontrado")
    return motorista_veiculo

@motorista_veiculo.put("/{id}")
async def atualizar_motorista_veiculo(id_motorista_veiculo: int, dados: MotoristaVeiculoResponse, db: Session = Depends(get_db)):
    motorista_veiculo = db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id_motorista_veiculo == id_motorista_veiculo).first()
    if not motorista_veiculo:
        raise HTTPException(status_code=404, detail="Motorista Veículo não encontrado")
    
    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(motorista_veiculo, chave, valor)
    
    db.commit()
    db.refresh(motorista_veiculo)
    return motorista_veiculo

@motorista_veiculo.delete("/{id}")
async def apagar_motorista_veiculo(id_motorista_veiculo: int, db: Session = Depends(get_db)):
    motorista_veiculo = db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id_motorista_veiculo == id_motorista_veiculo).first()
    if not motorista_veiculo:
        raise HTTPException(status_code=404, detail="Motorista Veículo não encontrado")
    
    db.delete(motorista_veiculo)
    db.commit()
    return {"message": "Motorista removido com sucesso"}