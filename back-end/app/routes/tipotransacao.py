from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.tipotransacao import TipoTransacao
from app.schemas import TipoTransacaoCreate, TipoTransacaoOut
from app.database.database import get_db
from app.auth import get_current_user

router = APIRouter()

@router.post("/tipotransacao", response_model=TipoTransacaoOut, tags=["tipoTransacao"])
def create_tipotransacao(tipo: TipoTransacaoCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_tipo = TipoTransacao(**tipo.dict())
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.get("/tipotransacao", response_model=list[TipoTransacaoOut], tags=["tipoTransacao"])
def list_tipotransacoes(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(TipoTransacao).all()

@router.get("/tipotransacao/{tipo_id}", response_model=TipoTransacaoOut, tags=["tipoTransacao"])
def get_tipotransacao(tipo_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    tipo = db.query(TipoTransacao).filter(TipoTransacao.id == tipo_id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="TipoTransacao não encontrada")
    return tipo

@router.put("/tipotransacao/{tipo_id}", response_model=TipoTransacaoOut, tags=["tipoTransacao"])
def update_tipotransacao(tipo_id: int, tipo: TipoTransacaoCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_tipo = db.query(TipoTransacao).filter(TipoTransacao.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="TipoTransacao não encontrada")
    for key, value in tipo.dict().items():
        setattr(db_tipo, key, value)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.delete("/tipotransacao/{tipo_id}", tags=["tipoTransacao"])
def delete_tipotransacao(tipo_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_tipo = db.query(TipoTransacao).filter(TipoTransacao.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="TipoTransacao não encontrada")
    db.delete(db_tipo)
    db.commit()
    return {"ok": True}
