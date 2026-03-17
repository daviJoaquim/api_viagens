from sqlalchemy import Column, Integer, Float, ForeignKey
from app.database import Base

class PassageiroModel(Base):
    __tablename__ = "passageiro"

    id_passageiro = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"))
    media_avaliacao = Column(Float)