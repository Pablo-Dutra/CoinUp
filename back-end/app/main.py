from fastapi import FastAPI
from app.routes import conta, categoria

app = FastAPI(title="CoinUp API", docs_url="/docs", redoc_url="/redoc")

app.include_router(conta.router)
app.include_router(categoria.router)
