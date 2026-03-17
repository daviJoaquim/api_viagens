from sqlalchemy import Column, ForeignKey, Integer, String
from app.database import Base

class VeiculoModel(Base):
    __tablename__ = "veiculo"

    id_veiculo = Column(Integer, primary_key=True, autoincrement=True)
    placa = Column (String(7))
    id_modelo = Column(Integer, ForeignKey("modelo.id_modelo_veiculo"))
    tem_seguro = Column(Integer)
    id_classe_veiculo = Column(Integer, ForeignKey("classe_veiculo.id_classe_veiculo"))