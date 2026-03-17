from pydantic import BaseModel
from datetime import datetime

class AvaliacaoSchema(BaseModel):
    nota_passageiro: float
    nota_motorista: float
    datahora_limite: datetime

class AvaliacaoResponse(AvaliacaoSchema):
    id_avaliacao: int

    class Config:
        from_attributes = True

