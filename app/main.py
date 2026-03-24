from fastapi import FastAPI
from app.route.usuario import usuario as rota_usuario

from app.route.tipo_combustivel import tipo_combustivel as rota_tipo_combustivel
from app.route.classe import classe as rota_classe
from app.route.metodo_pagamento import metodo_pagamento as rota_metodo_pagamentos
from app.route.servico import servico as rota_servico

from app.route.modelo_veiculo import modelo_veiculo as rota_modelo_veiculo

from app.route.passageiro import passageiro as rota_passageiro
from app.route.motorista import motorista as rota_motorista

from app.route.veiculo import veiculo as rota_veiculo
from app.route.motorista_veiculo import motorista_veiculo as rota_motorista_veiculo

from app.route.corrida import corrida as rota_corrida

from app.route.pagamentos import pagamentos as rota_pagamentos
from app.route.avaliacao import avaliacao as rota_avaliacao
from app.database import Base, engine

#Criar todas as entidades no banco de dados
#Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(rota_usuario)

app.include_router(rota_tipo_combustivel)
app.include_router(rota_classe)
app.include_router(rota_metodo_pagamentos)
app.include_router(rota_servico)

app.include_router(rota_modelo_veiculo)

app.include_router(rota_passageiro)
app.include_router(rota_motorista)

app.include_router(rota_veiculo)
app.include_router(rota_motorista_veiculo)

app.include_router(rota_corrida)

app.include_router(rota_pagamentos)
app.include_router(rota_avaliacao)
