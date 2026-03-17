from pydantic import BaseModel
from typing import Optional

class MotoristaSchema(BaseModel):
    id_usuario: int
    media_avaliacao: Optional[float]
    cnh: int

class MotoristaResponse(MotoristaSchema):
    id_motorista: int

    class Config:
        from_attributes = True