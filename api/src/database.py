'''
configurações do sqlalchemy:
Engine: se conecta ao arquivo sqlite.db
SessionLocal: A fábrica que criará "sessões" de conversa com o banco de dados.
Base: A classe "mãe" da qual todos os modelos (tabelas) irão herdar.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Define a URL do banco de dados
# - "sqlite:///" -> Use o driver do SQLite
db_name = "cards"
SQLALCHEMY_DATABASE_URL = f"sqlite:///./{db_name}.db"

# Cria a engine do sqlalchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args é necessário apenas para o SQLite, para permitir multithread
    connect_args={"check_same_thread": False},
    )

# fábrica de sessões 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa
# modelos de dados vão herdar dessa classe
Base = declarative_base()