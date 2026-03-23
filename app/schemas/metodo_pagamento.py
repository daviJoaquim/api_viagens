from pydantic import BaseModel

class MetodoPagamentoSchema(BaseModel):
    descricao: str
    nome_financeira: int

class MetodoPagamentoResponse(MetodoPagamentoSchema):
    id_metodo_pagamento: int

    class Config:
        from_attributes = True

    