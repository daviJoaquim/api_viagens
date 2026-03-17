from pydantic import BaseModel

class VeiculoModel(BaseModel):
    placa: str
    id_modelo_veiculo : int
    tem_seguro : int
    id_classe_veiculo: int

class VeiculoResponse(VeiculoModel):
    id_veiculo: int

    class Config:
        from_attributes = True 