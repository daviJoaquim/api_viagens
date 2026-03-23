from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from os import getenv
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# ---------------------------------------------------------
# 1. CONEXÃO COM O SERVIDOR MYSQL (SEM BANCO ESPECÍFICO)
# ---------------------------------------------------------
# Usada apenas para criar o banco de dados caso ele não exista
SERVER_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PSWD')}@{getenv('DB_HOST')}"

# Cria o engine responsável por conectar ao servidor MySQL
engine_server = create_engine(SERVER_URL)

# Cria o banco de dados caso ele ainda não exista
with engine_server.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {getenv('DB_NAME')}"))
    conn.commit()

# ---------------------------------------------------------
# 2. CONEXÃO COM O BANCO DE DADOS DA APLICAÇÃO
# ---------------------------------------------------------
# URL completa agora incluindo o nome do banco criado
DATABASE_URL = f"mysql+pymysql://{getenv('DB_USER')}:{getenv('DB_PSWD')}@{getenv('DB_HOST')}/{getenv('DB_NAME')}"

# Engine principal que gerencia as conexões com o banco da aplicação
engine = create_engine(DATABASE_URL)

# ---------------------------------------------------------
# 3. CONFIGURAÇÃO DA SESSÃO DO SQLALCHEMY
# ---------------------------------------------------------
# A sessão será utilizada para executar comandos SQL (CRUD)
SessionLocal = sessionmaker(
    autocommit=False,  # Não faz commit automático
    autoflush=False,   # Não envia alterações automaticamente ao banco
    bind=engine        # Associa a sessão ao engine criado
)

# ---------------------------------------------------------
# 4. BASE PARA CRIAÇÃO DOS MODELOS (ORM)
# ---------------------------------------------------------
# Todas as tabelas do projeto irão herdar dessa base
class Base(DeclarativeBase):
    pass

# ---------------------------------------------------------
# 5. DEPENDÊNCIA DE BANCO DE DADOS (FASTAPI)
# ---------------------------------------------------------
# Função utilizada para injetar a sessão do banco em cada rota
# garantindo abertura e fechamento correto da conexão
def get_db():
    db = SessionLocal()
    try:
        yield db  # Entrega a sessão para a rota usar
    finally:
        db.close()  # Fecha a conexão após o uso