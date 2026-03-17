from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MotoristaVeiculoModel(BaseModel):
    id_motorista: int 
    id_veiculo: int
    datahora_inicio: Optional[datetime]
    datahora_fim: Optional[datetime]

    class Config:
        from_attributes = True