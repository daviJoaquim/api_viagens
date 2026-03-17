from pydantic import BaseModel

class ClasseSchema(BaseModel):
    nome_classe: str
    fator_preco: float

class ClasseResponse(ClasseSchema):
    id_classe: int

    class Config:
        from_attributes = True
    