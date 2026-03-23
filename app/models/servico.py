from sqlalchemy import Column, ForeignKey, Integer, String
from app.database import Base

class ServicoModel(Base):
    __tablename__ = "servico"

    id_servico = Column(Integer, primary_key=True, autoincrement=True)
    nome_servico = Column(String(50))
    id_classe = Column(Integer, ForeignKey ("classe.id_classe"))