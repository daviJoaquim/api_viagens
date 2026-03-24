from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class ModeloVeiculoModel(Base):
    __tablename__ = "modelo_veiculo"

    id_modelo_veiculo = Column(Integer, primary_key=True, autoincrement=True)
    id_tipo_combustivel = Column(Integer, ForeignKey("tipo_combustivel.id_tipo_combustivel"), nullable=False)
    modelo = Column(String(100), nullable=False)
    cor = Column(String(50))
    ano = Column(Integer)
    propriedade = Column(String(45))
    capacidade = Column(Integer) 
