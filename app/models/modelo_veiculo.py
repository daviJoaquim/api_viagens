from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class ModeloVeiculoModel(Base):
    __tablename__ = "modelo_veiculo"

    id_modelo_veiculo = Column(Integer, primary_key=True, autoincrement=True)
    id_veiculo = Column(Integer, ForeignKey("veiculo.id_veiculo"))
    id_motorista = Column(Integer, ForeignKey("motorista.id_motorista"), nullable=False)
    id_tipo_combustivel = Column(Integer, ForeignKey("tipo_combustivel.id_combustivel"), nullable=False)
    modelo = Column(String(100), nullable=False)
    marca = Column(String(100), nullable=False)
    placa = Column(String(10), nullable=False)
    cor = Column(String(50))
    ano = Column(Integer)
    propriedade = Column(Integer)
    capacidade = Column(String(20)) 
