from sqlalchemy import Column, ForeignKey, Integer, String
from app.database import Base

class VeiculoModel(Base):
    __tablename__ = "veiculo"

    id_veiculo = Column(Integer, primary_key=True, autoincrement=True)
    placa = Column (String(7))
    id_modelo_veiculo = Column(Integer, ForeignKey("modelo_veiculo.id_modelo_veiculo"))
    tem_seguro = Column(Integer)
    id_classe = Column(Integer, ForeignKey("classe.id_classe"))