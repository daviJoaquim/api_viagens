from sqlalchemy import DECIMAL, Column, Integer, DateTime, ForeignKey, String
from app.database import Base

class CorridaModel(Base):
    __tablename__ = "corrida"

    id_corrida = Column(Integer, primary_key=True, autoincrement=True)
    id_passageiro = Column(Integer, ForeignKey("passageiro.id_passageiro"), nullable=False)
    id_motorista = Column(Integer, ForeignKey("motorista.id_motorista"), nullable=False)
    id_servico = Column(Integer, ForeignKey("servico.id_servico"))
    id_avaliacao = Column(Integer, ForeignKey("avaliacao.id_avaliacao"))
    data_inicio = Column(DateTime)
    data_fim = Column(DateTime)
    local_partida= Column(String(50))
    local_destino = Column(String(50))
    valor = Column(DECIMAL(10,2))
    status = Column(String(30))