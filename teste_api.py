import requests


def testar_api():
    url = "http://localhost:8000/chat"

    # Pergunta 1: Conversa normal
    print("\n--- Teste 1: Conversa Geral ---")
    msg1 = {"message": "Olá! Quem é você?"}
    resp1 = requests.post(url, json=msg1).json()
    print(f"Você: {msg1['message']}")
    print(f"IA: {resp1['response']}")

    # Pergunta 2: Cálculo (O teste de fogo!)
    print("\n--- Teste 2: Cálculo Matemático ---")
    # O agente deve detectar e usar a Tool
    msg2 = {"message": "Quanto é 100 * 50?"}
    resp2 = requests.post(url, json=msg2).json()
    print(f"Você: {msg2['message']}")
    print(f"IA: {resp2['response']}")


if __name__ == "__main__":
    testar_api()
