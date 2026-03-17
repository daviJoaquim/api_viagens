from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class MotoristaVeiculoModel(Base):
    __tablename__ = "motorista-veiculo"

    id_motorista = Column(Integer, primary_key=True, autoincrement=True)
    id_veiculo = Column(Integer, primary_key=True, autoincrement=True)
    datahora_inicio = Column(DateTime)
    datahora_fim = Column(DateTime)