from fastapi import FastAPI
from app.route import avaliacao, classe, motorista, pagamentos, passageiro, servico, usuario

from app.database import Base, engine

#Criar todas as entidades no banco de dados
Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(usuario.viagens)
app.include_router(avaliacao.viagens)
app.include_router(classe.viagens)
app.include_router(motorista.viagens)
app.include_router(pagamentos.viagens)
app.include_router(passageiro.viagens)
app.include_router(servico.viagens)
