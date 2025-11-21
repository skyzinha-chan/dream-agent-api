import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para a memória
load_dotenv()


class Settings:
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Dream Agent")
    VERSION: str = os.getenv("VERSION", "1.0.0")

    # Configurações do Ollama
    OLLAMA_BASE_URL: str = os.getenv(
        "OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3.2")


# Instância única para ser importada em outros arquivos
settings = Settings()
