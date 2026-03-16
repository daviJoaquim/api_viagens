from fastapi import FastAPI
from app.database import Base, engine
from app.route.viagens import viagens

#Criar todas as entidades no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(viagens)

@app.get("/")
async def health_check():
    return {"status": "API Online"}