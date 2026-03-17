from sqlalchemy import DECIMAL, Column, Integer, String, DateTime
from app.database import Base

class AvaliacaoModel(Base):
    __tablename__ = "avaliacao"
    
    id_avaliacao = Column(Integer, primary_key=True, autoincrement=True)
    nota_passageiro = Column(DECIMAL (3,2))
    nota_motorista = Column(DECIMAL (3,2))
    datahora_limite = Column(DateTime)