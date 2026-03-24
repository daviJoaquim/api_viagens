from pydantic import BaseModel
from datetime import date

class UsuarioSchema(BaseModel):
    nome: str
    cpf: str
    data_nascimento: date
    email: str
    usuario: str
    senha: str

class UsuarioResponse(UsuarioSchema):
    id: int

    class Config: 
        from_attributes = True