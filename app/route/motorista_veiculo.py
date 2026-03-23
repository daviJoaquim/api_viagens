from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.motorista_veiculo import MotoristaVeiculoModel
from app.schemas.motorista_veiculo import MotoristaVeiculoResponse, MotoristaVeiculoSchema

viagens = APIRouter(prefix="/motorista_veiculo", tags=["motorista_veiculo"])

@viagens.post("/", response_model= MotoristaVeiculoResponse)
async def criar_motorista_veiculo(dados: MotoristaVeiculoSchema, db: Session = Depends(get_db)):

    criar_motorista_veiculo = MotoristaVeiculoModel(**dados.model_dump())
    db.add(criar_motorista_veiculo)
    db.commit()
    db.refresh(criar_motorista_veiculo)
    return criar_motorista_veiculo

@viagens.get("/", response_model=list[MotoristaVeiculoResponse])
async def listar_motorista_veiculo(db:Session = Depends(get_db)):
    return db.query(MotoristaVeiculoModel).all()

@viagens.get("/{id}", response_model=MotoristaVeiculoResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    motorista_veiculo = db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id_motorista_veiculo == id).first()
    
    if not motorista_veiculo:
        raise HTTPException(404, "Não encontrado")
    return motorista_veiculo

@viagens.put("/{id}", response_model= MotoristaVeiculoResponse)
async def atualizar_motorista_veiculo(id: int, dados: MotoristaVeiculoSchema, db: Session = Depends(get_db)):
   motorista_veiculo = db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id_motorista_veiculo == id).first()

   if not motorista_veiculo: 
       raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Modelo veículo com ID {id} não encontrada"
        )
   
   for campo, valor in dados.model_dump().items():
       setattr(motorista_veiculo, campo, valor)

   db.commit()
   db.refresh(motorista_veiculo)

   return motorista_veiculo

@viagens.delete("/{id}")
async def deletar_motorista_veiculo(id: int, db:Session= Depends(get_db)):
    modelo_veiculo = db.query(MotoristaVeiculoModel).filter(MotoristaVeiculoModel.id_motorista_veiculo == id).first()

    if not modelo_veiculo:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"O motorista veículo com ID {id} não foi encontrada"
        )

        
    db.delete(modelo_veiculo)
    db.commit()
    return("Deletado com sucesso!")


