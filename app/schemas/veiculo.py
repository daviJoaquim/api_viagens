from pydantic import BaseModel

class VeiculoSchema(BaseModel):
    placa: str
    id_modelo_veiculo : int
    tem_seguro : bool
    id_classe: int

class VeiculoResponse(VeiculoSchema):
    id_veiculo: int

    class Config:
        from_attributes = True 