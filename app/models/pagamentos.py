from sqlalchemy import DECIMAL, Column, Integer, String, ForeignKey, DateTime
from app.database import Base

class PagamentosModel(Base):
    __tablename__ = "pagamento"

    id_pagamento = Column(Integer, primary_key=True, autoincrement=True)
    id_corrida = Column(Integer, ForeignKey ("corrida.id_corrida"))
    valor = Column(DECIMAL (3,2))
    id_metodo_pagamento = Column (Integer, ForeignKey ("metodo_pagamento.id_metodo_pagamento"))
    datahora_transicao = Column (DateTime)
