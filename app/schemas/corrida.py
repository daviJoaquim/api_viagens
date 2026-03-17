from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CorridaMOdel(BaseModel):
    id_passgeiro: int
    id_motorista: int
    id_servico: int
    id_avaliacao: Optional[float]
    datahora_inicio: datetime
    datahora_fim: Optional[datetime]
    local_partida: str
    local_destino: str
    valor: float
    status: str
