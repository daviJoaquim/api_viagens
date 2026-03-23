from sqlalchemy import Column, Integer, DateTime, ForeignKey
from app.database import Base

class MotoristaVeiculoModel(Base):
    __tablename__ = "motorista_veiculo"

    id_motorista_veiculo = Column(Integer, primary_key=True, autoincrement=True)

    id_motorista = Column(Integer, ForeignKey("motorista.id_motorista"))
    id_veiculo = Column(Integer, ForeignKey("veiculo.id_veiculo"))

    datahora_inicio = Column(DateTime)
    datahora_fim = Column(DateTime)