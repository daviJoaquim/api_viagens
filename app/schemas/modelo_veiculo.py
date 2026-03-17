from pydantic import BaseModel

class ModeloVeiculoModel(BaseModel):
    nome_modelo: str
    fabricante: str
    cor: str
    ano: int
    capacidade: int
    propriedade: str
    id_tipo_combustivel: int

class ModeloVeiculoResponse(ModeloVeiculoModel):
    id_modelo_veiculo: int

    class Config:
        from_attributes = True