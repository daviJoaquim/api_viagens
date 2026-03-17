from sqlalchemy import Column, ForeignKey, Integer, String
from app.database import Base

class ServicoModel(Base):
    __tablename__ = "servico"

    id_servico = Column(Integer, primary_key=True, autoincrement=True)
    nome_servico = Column(String(50))
    id_classe_minima = Column(Integer, ForeignKey ("classe_minima.id_classe"))