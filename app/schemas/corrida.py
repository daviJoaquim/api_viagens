from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CorridaSchema(BaseModel):
    id_passageiro: int
    id_motorista: int
    id_servico: int
    id_avaliacao: Optional[float]
    datahora_inicio: datetime
    datahora_fim: Optional[datetime]
    local_partida: str
    local_destino: str
    valor: float
    status: str

class CorridaResponse(CorridaSchema):
    id_corrida: int

    class Config:
        from_attributes = True
