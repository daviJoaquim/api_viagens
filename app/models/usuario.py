from sqlalchemy import Column, Integer, String
from app.database import Base

class UsuarioModel(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome =
    cpf =
    data_nascimento =
    idade =
    senha =
    email =
    usuario =