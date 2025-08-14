from sqlalchemy import Column, Integer, String, Boolean
from app.database.database import Base

class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String, nullable=False)
    ativo = Column(Boolean, default=True)
