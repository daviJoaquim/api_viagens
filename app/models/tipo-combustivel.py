from sqlalchemy import DECIMAL, Column, Integer, String
from app.database import Base

class TipoCombustivelModel(Base):
    __tablename__ = "tipo-combustivel"

    id_combustivel = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(50))
    fator_carbono = Column(DECIMAL (10,5))
