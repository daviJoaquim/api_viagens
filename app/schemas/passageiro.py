from pydantic import BaseModel
from typing import Optional

class PassageiroSchema(BaseModel):
    id_usuario: int
    media_avaliacao: Optional[float]

class PassageiroResponse(PassageiroSchema):
    id_passageiro: int

    class Config:
        from_attributes = True