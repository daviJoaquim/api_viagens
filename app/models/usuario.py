from sqlalchemy import Column, Integer, String, Date
from app.database import Base

class UsuarioModel(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(11))
    data_nascimento = Column(Date)
    senha = Column(String(64), nullable=False)
    email = Column(String(64), unique=True, nullable=False)
    usuario = Column(String(50), unique=True, nullable=False)