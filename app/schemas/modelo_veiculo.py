from pydantic import BaseModel

class ModeloVeiculoSchema(BaseModel):
    nome_modelo: str
    fabricante: str
    cor: str
    ano: int
    capacidade: int
    propriedade: str
    id_tipo_combustivel: int

class ModeloVeiculoResponse(ModeloVeiculoSchema):
    id_modelo_veiculo: int

    class Config:
        from_attributes = True