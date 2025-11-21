from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import router as api_router

# Inicializa a aplicação
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="API de Chat com Agente Inteligente e Tools Matemáticas"
)

# Inclui as rotas (endpoints)
app.include_router(api_router)


@app.get("/")
def root():
    """Rota de verificação de saúde (Health Check)"""
    return {"status": "online", "message": "Bem-vindo ao Dream Agent API"}


# Bloco para execução direta (opcional, mas útil para debug)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
