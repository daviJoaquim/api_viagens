from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MotoristaVeiculoSchema(BaseModel):
    id_motorista: int 
    id_veiculo: int
    datahora_inicio: Optional[datetime]
    datahora_fim: Optional[datetime]


class MotoristaVeiculoResponse(MotoristaVeiculoSchema):
    id_motorista_veiculo: int
    
    class Config:
        from_attributes = True
