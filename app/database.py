from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# inicialização (Criação do SCHEMA no banco de dadoss)
SERVER_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PSWD')}@{getenv('DB_HOST')}"

engine_server = create_engine(SERVER_URL)

with engine_server.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {getenv('DB_NAME')}"))
    conn.commit()

# DATABASE_URL = "mysql+pymysql://root:admin@localhost/series_api"
DATABASE_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PSWD')}@{getenv('DB_HOST')}/{getenv('DB_NAME')}"

# Criar um "motor" que fará o gerenciamento da conexão
engine = create_engine(DATABASE_URL)

#Criando uma sessão para executar os comandos SQL
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Cria um objeto da base dde dados manipulável pelo Python
Base = declarative_base()

#Injeção de dependência: injeta a sessão de dados
# em cada rota que for criada
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
