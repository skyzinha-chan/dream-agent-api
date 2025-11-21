import logging
from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import router as api_router

# --- CONFIGURAÇÃO DE LOGS (Técnica de Sênior) ---
# Isso configura para que os prints tenham data, hora e nível de severidade.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# Inicializa a aplicação
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="API de Chat com Agente Inteligente e Tools Matemáticas"
)

app.include_router(api_router)


@app.on_event("startup")
async def startup_event():
    logger.info("🚀 Iniciando Dream Agent API...")
    logger.info(f"🔧 Modelo Carregado: {settings.OLLAMA_MODEL}")


@app.get("/")
def root():
    return {"status": "online", "message": "Bem-vindo ao Dream Agent API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
    logger.info("API rodando em http://localhost:8000")