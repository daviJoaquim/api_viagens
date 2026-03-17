from sqlalchemy import DECIMAL, Column, Integer, String
from app.database import Base

class ClasseModel(Base):
    __tablename__ = "classe"

    id_classe = Column(Integer, primary_key=True, autoincrement=True)
    nome_classe =  Column(String(45))
    fator_preco = Column(DECIMAL(10,2))
