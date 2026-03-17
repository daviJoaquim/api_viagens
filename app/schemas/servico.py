from pydantic import BaseModel

class ServicoSchema(BaseModel):
    nome_servico: str
    id_classe_minima: int

class ServicoResponse(ServicoSchema):
    id_servico : int

    class Config:
        from_attributes = True

    