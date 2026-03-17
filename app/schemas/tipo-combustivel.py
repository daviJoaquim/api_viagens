from pydantic import BaseModel

class TipoCombustivelModel(BaseModel):
    descricao: str
    fator_carbono: float

class TipoCombustivelResponse(TipoCombustivelModel):
    id_tipo_combustivel : int

    class Config :
        from_atrributes = True
