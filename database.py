from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ATENÇÃO: Troque 'postgres123' pela sua senha real
DATABASE_URL = "postgresql://postgres:postgres123@localhost:5432/engenharia_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Função para pegar uma sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()