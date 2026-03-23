from pydantic import BaseModel

class TipoCombustivelSchema(BaseModel):
    descricao: str
    fator_carbono: float

class TipoCombustivelResponse(TipoCombustivelSchema):
    id_tipo_combustivel : int

    class Config :
        from_atrributes = True
