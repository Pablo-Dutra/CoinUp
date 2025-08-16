from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.usuario import Usuario
from app.schemas import Token
from app.auth import create_access_token, get_current_user
from fastapi.middleware.cors import CORSMiddleware
from app.routes import conta, categoria, lancamento
import hashlib

app = FastAPI(title="CoinUp API", docs_url="/docs", redoc_url="/redoc")

app.include_router(conta.router)
app.include_router(categoria.router)
app.include_router(lancamento.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/login", response_model=Token, tags=["Autenticação"])
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
	user = db.query(Usuario).filter(Usuario.email == form_data.username).first()
	if not user or user.password != hashlib.sha256(form_data.password.encode()).hexdigest():
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email ou senha inválidos")
	access_token = create_access_token(data={"sub": user.email})
	return {"access_token": access_token, "token_type": "bearer"}

@app.post("/logout", tags=["Autenticação"])
def logout():
	return {"message": "Logout realizado. Descarte o token no cliente."}