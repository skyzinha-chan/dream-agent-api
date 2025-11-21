import requests
import json

# Configuração simples para testar se o Ollama está ouvindo
# Por padrão, o Ollama roda na porta 11434
OLLAMA_URL = "http://localhost:11434/api/generate"


def testar_ollama():
    payload = {
        "model": "llama3.2",  # Certifique-se que este é o modelo que você baixou
        "prompt": "Responda apenas com a palavra 'FUNCIONOU' se você estiver me ouvindo.",
        "stream": False
    }

    try:
        print("📡 Tentando conectar com o Ollama local...")
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()

        resposta_ia = response.json().get("response", "").strip()
        print(f"🤖 Resposta da IA: {resposta_ia}")
        print("✅ Sucesso! O ambiente está pronto.")

    except requests.exceptions.ConnectionError:
        print("❌ Erro: Não foi possível conectar ao Ollama.")
        print("Dica: Verifique se o aplicativo do Ollama está rodando.")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")


if __name__ == "__main__":
    testar_ollama()
# Para rodar este script, use o comando:
# python teste_conexao.py