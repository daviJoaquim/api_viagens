from pydantic import BaseModel
from datetime import datetime

class PagamentoSchema(BaseModel):
    id_corrida: int
    valor: float
    id_metodo_pagamento: int
    datahora_transacao: datetime

class PagamentoResponse(PagamentoSchema):
    id_pagamento: int

    class Config:
        from_attributes = True