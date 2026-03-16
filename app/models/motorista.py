from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

class MotoristaModel(Base):
    __tablename__ = "motoristas"

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"))
    media_avaliacao = Column(Float)
    cnh = Column(String(20))