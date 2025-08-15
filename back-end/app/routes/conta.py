from app.models.conta import TipoConta
from app.schemas import TipoContaCreate, TipoContaOut
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.conta import Conta
from app.schemas import ContaBase, ContaCreate, ContaOut
from app.auth import get_current_user

router = APIRouter()


# CRUD Conta
@router.post("/conta", response_model=ContaOut, tags=["contas"])
def create_conta(conta: ContaCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_conta = Conta(**conta.dict())
    db.add(db_conta)
    db.commit()
    db.refresh(db_conta)
    return db_conta

@router.get("/conta", response_model=list[ContaOut], tags=["contas"])
def list_contas(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(Conta).all()

@router.get("/conta/{conta_id}", response_model=ContaOut, tags=["contas"])
def get_conta(conta_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    conta = db.query(Conta).filter(Conta.id == conta_id).first()
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    return conta

@router.put("/conta/{conta_id}", response_model=ContaOut, tags=["contas"])
def update_conta(conta_id: int, conta: ContaCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_conta = db.query(Conta).filter(Conta.id == conta_id).first()
    if not db_conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    for key, value in conta.dict().items():
        setattr(db_conta, key, value)
    db.commit()
    db.refresh(db_conta)
    return db_conta

@router.delete("/conta/{conta_id}", tags=["contas"])
def delete_conta(conta_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_conta = db.query(Conta).filter(Conta.id == conta_id).first()
    if not db_conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")
    db.delete(db_conta)
    db.commit()
    return {"ok": True}

# CRUD TipoConta
@router.post("/tipoconta", response_model=TipoContaOut, tags=["tipoContas"])
def create_tipoconta(tipo: TipoContaCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_tipo = TipoConta(**tipo.dict())
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.get("/tipoconta", response_model=list[TipoContaOut], tags=["tipoContas"])
def list_tipocontas(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(TipoConta).all()

@router.get("/tipoconta/{tipo_id}", response_model=TipoContaOut, tags=["tipoContas"])
def get_tipoconta(tipo_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    tipo = db.query(TipoConta).filter(TipoConta.id == tipo_id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="TipoConta não encontrada")
    return tipo

@router.put("/tipoconta/{tipo_id}", response_model=TipoContaOut, tags=["tipoContas"])
def update_tipoconta(tipo_id: int, tipo: TipoContaCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_tipo = db.query(TipoConta).filter(TipoConta.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="TipoConta não encontrada")
    for key, value in tipo.dict().items():
        setattr(db_tipo, key, value)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.delete("/tipoconta/{tipo_id}", tags=["tipoContas"])
def delete_tipoconta(tipo_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_tipo = db.query(TipoConta).filter(TipoConta.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="TipoConta não encontrada")
    db.delete(db_tipo)
    db.commit()
    return {"ok": True}