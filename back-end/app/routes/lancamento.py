from app.models.lancamento import TipoTransacao
from app.schemas import TipoTransacaoCreate, TipoTransacaoOut
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.lancamento import Lancamento
from app.schemas import LancamentoCreate, LancamentoOut, LancamentoDetalhadoOut
from app.database.database import get_db
from app.auth import get_current_user

router = APIRouter()

@router.post("/lancamentos", response_model=LancamentoOut, tags=["Lançamentos"])
def create_lancamento(lancamento: LancamentoCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_lancamento = Lancamento(**lancamento.dict())
    db.add(db_lancamento)
    db.commit()
    db.refresh(db_lancamento)
    return db_lancamento

@router.get("/lancamentos", response_model=list[LancamentoDetalhadoOut], tags=["Lançamentos"])
def list_lancamentos(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    lancamentos = db.query(Lancamento).all()
    result = []
    for l in lancamentos:
        result.append(LancamentoDetalhadoOut(
            id=l.id,
            idReferencia=l.idReferencia,
            idCategoria=l.idCategoria,
            idConta=l.idConta,
            idTipoTransacao=l.idTipoTransacao,
            dataLancamento=l.dataLancamento,
            dataTransacao=l.dataTransacao,
            descricao=l.descricao,
            valor=l.valor,
            categoria_descricao=l.categoria.descricao if l.categoria else None,
            conta_nome=l.conta.nome if l.conta else None,
            tipoconta_descricao=l.conta.tipo.descricao if l.conta and l.conta.tipo else None,
            tipotransacao_descricao=l.tipotransacao.descricao if l.tipotransacao else None
        ))
    return result

@router.get("/lancamentos/{lancamento_id}", response_model=LancamentoDetalhadoOut, tags=["Lançamentos"])
def get_lancamento(lancamento_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    l = db.query(Lancamento).filter(Lancamento.id == lancamento_id).first()
    if not l:
        raise HTTPException(status_code=404, detail="Lancamento não encontrado")
    return LancamentoDetalhadoOut(
        id=l.id,
        idReferencia=l.idReferencia,
        idCategoria=l.idCategoria,
        idConta=l.idConta,
        idTipoTransacao=l.idTipoTransacao,
        dataLancamento=l.dataLancamento,
        dataTransacao=l.dataTransacao,
        descricao=l.descricao,
        valor=l.valor,
        categoria_descricao=l.categoria.descricao if l.categoria else None,
        conta_nome=l.conta.nome if l.conta else None,
        tipoconta_descricao=l.conta.tipo.descricao if l.conta and l.conta.tipo else None,
        tipotransacao_descricao=l.tipotransacao.descricao if l.tipotransacao else None
    )

@router.put("/lancamentos/{lancamento_id}", response_model=LancamentoOut, tags=["Lançamentos"])
def update_lancamento(lancamento_id: int, lancamento: LancamentoCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_lancamento = db.query(Lancamento).filter(Lancamento.id == lancamento_id).first()
    if not db_lancamento:
        raise HTTPException(status_code=404, detail="Lancamento não encontrado")
    for key, value in lancamento.dict().items():
        setattr(db_lancamento, key, value)
    db.commit()
    db.refresh(db_lancamento)
    return db_lancamento

@router.delete("/lancamentos/{lancamento_id}", tags=["Lançamentos"])
def delete_lancamento(lancamento_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_lancamento = db.query(Lancamento).filter(Lancamento.id == lancamento_id).first()
    if not db_lancamento:
        raise HTTPException(status_code=404, detail="Lancamento não encontrado")
    db.delete(db_lancamento)
    db.commit()
    return {"ok": True}

# CRUD TipoTransacao
@router.post("/tipotransacao", response_model=TipoTransacaoOut, tags=["Lançamentos"])
def create_tipotransacao(tipo: TipoTransacaoCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_tipo = TipoTransacao(**tipo.dict())
    db.add(db_tipo)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.get("/tipotransacao", response_model=list[TipoTransacaoOut], tags=["Lançamentos"])
def list_tipotransacoes(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(TipoTransacao).all()

@router.get("/tipotransacao/{tipo_id}", response_model=TipoTransacaoOut, tags=["Lançamentos"])
def get_tipotransacao(tipo_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    tipo = db.query(TipoTransacao).filter(TipoTransacao.id == tipo_id).first()
    if not tipo:
        raise HTTPException(status_code=404, detail="TipoTransacao não encontrada")
    return tipo

@router.put("/tipotransacao/{tipo_id}", response_model=TipoTransacaoOut, tags=["Lançamentos"])
def update_tipotransacao(tipo_id: int, tipo: TipoTransacaoCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_tipo = db.query(TipoTransacao).filter(TipoTransacao.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="TipoTransacao não encontrada")
    for key, value in tipo.dict().items():
        setattr(db_tipo, key, value)
    db.commit()
    db.refresh(db_tipo)
    return db_tipo

@router.delete("/tipotransacao/{tipo_id}", tags=["Lançamentos"])
def delete_tipotransacao(tipo_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_tipo = db.query(TipoTransacao).filter(TipoTransacao.id == tipo_id).first()
    if not db_tipo:
        raise HTTPException(status_code=404, detail="TipoTransacao não encontrada")
    db.delete(db_tipo)
    db.commit()
    return {"ok": True}