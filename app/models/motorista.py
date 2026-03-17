from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from app.database import Base

class MotoristaModel(Base):
    __tablename__ = "motorista"

    id_motorista = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"))
    media_avaliacao = Column(DECIMAL(3,2))
    cnh = Column(String(20))