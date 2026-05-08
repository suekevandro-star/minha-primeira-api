from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

from database import SessionLocal, get_db, engine, Base
import models  # <--- IMPORTANTE: Importa os modelos

# --- CRIA AS TABELAS NO BANCO AO INICIAR ---
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Engenharia")

# --- Esquemas de Validação (Pydantic) ---
class EngenheiroCreate(BaseModel):
    nome: str
    especialidade: str
    registro_crea: str

class EngenheiroResponse(EngenheiroCreate):
    id: int
    class Config:
        from_attributes = True

# --- Rotas da API ---

@app.post("/engenheiros/", response_model=EngenheiroResponse, status_code=status.HTTP_201_CREATED)
def criar_engenheiro(engenheiro: EngenheiroCreate, db: Session = Depends(get_db)):
    """Cadastra um novo engenheiro no banco"""
    db_eng = models.Engenheiro(**engenheiro.model_dump())
    db.add(db_eng)
    db.commit()
    db.refresh(db_eng)
    return db_eng

@app.get("/engenheiros/", response_model=List[EngenheiroResponse])
def listar_engenheiros(db: Session = Depends(get_db)):
    """Retorna todos os engenheiros cadastrados"""
    return db.query(models.Engenheiro).all()

@app.get("/")
def raiz():
    return {"mensagem": "Olá, Engenheiro! Sua API com PostgreSQL está rodando."}

@app.get("/engenharia")
def engenharia():
    return {"status": "Operacional", "tensao": "220V", "frequencia": "60Hz"}