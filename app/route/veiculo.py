from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.veiculo import VeiculoModel
from app.schemas.veiculo import VeiculoSchema, VeiculoResponse

veiculo = APIRouter(prefix="/veiculo",tags=["Veículo"])

@veiculo.post("/", response_model=VeiculoSchema)
async def criar_veiculo(dados: VeiculoSchema, db: Session = Depends(get_db)):
    criar_veiculo = VeiculoModel(**dados.model_dump())
    db.add(criar_veiculo)
    db.commit()
    db.refresh(criar_veiculo)
    return criar_veiculo

@veiculo.get("/")
async def listar_veiculos(db: Session = Depends(get_db)):
    return db.query(VeiculoModel).all()

@veiculo.get("/{id}")
async def buscar_veiculo(id_veiculo: int, db: Session = Depends(get_db)):
    veiculo = db.query(VeiculoModel).filter(VeiculoModel.id_veiculo == id_veiculo).first()
    if not veiculo:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    return veiculo

@veiculo.put("/{id}")
async def atualizar_veiculo(id_veiculo: int, dados: VeiculoResponse, db: Session = Depends(get_db)):
    veiculo = db.query(VeiculoModel).filter(VeiculoModel.id_veiculo == id_veiculo).first()
    if not veiculo:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    
    for chave, valor in dados.model_dump(exclude_unset=True).items():
        setattr(veiculo, chave, valor)
    
    db.commit()
    db.refresh(veiculo)
    return veiculo

@veiculo.delete("/{id}")
async def apagar_veiculo(id_veiculo: int, db: Session = Depends(get_db)):
    veiculo = db.query(VeiculoModel).filter(VeiculoModel.id_veiculo == id_veiculo).first()
    if not veiculo:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")
    
    db.delete(veiculo)
    db.commit()
    return {"message": "Veículo removido com sucesso"}