from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.categoria import Categoria
from app.schemas import CategoriaCreate, CategoriaOut

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/categoria", response_model=CategoriaOut, tags=["Categorias"])
def create_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    db_categoria = Categoria(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

@router.get("/categoria", response_model=list[CategoriaOut], tags=["Categorias"])
def list_categorias(db: Session = Depends(get_db)):
    return db.query(Categoria).all()

@router.get("/categoria/{categoria_id}", response_model=CategoriaOut, tags=["Categorias"])
def get_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria

@router.put("/categoria/{categoria_id}", response_model=CategoriaOut, tags=["Categorias"])
def update_categoria(categoria_id: int, categoria: CategoriaCreate, db: Session = Depends(get_db)):
    db_categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if not db_categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    for key, value in categoria.dict().items():
        setattr(db_categoria, key, value)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

@router.delete("/categoria/{categoria_id}", tags=["Categorias"])
def delete_categoria(categoria_id: int, db: Session = Depends(get_db)):
    db_categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if not db_categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    db.delete(db_categoria)
    db.commit()
    return {"ok": True}
