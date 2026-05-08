from sqlalchemy import Column, Integer, String
from database import Base

class Engenheiro(Base):
    __tablename__ = "engenheiros"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    especialidade = Column(String)
    registro_crea = Column(String, unique=True, index=True)