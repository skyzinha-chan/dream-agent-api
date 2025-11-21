import requests


def testar_calculadora():
    url = "http://localhost:8000/chat"

    # Lista de perguntas para desafiar a IA e a Tool
    testes = [
        # 1. Decimais e Soma
        "Quanto é 50.5 + 10.2?",

        # 2. Prioridade Matemática (Parênteses)
        "Quanto é (10 + 2) * 5?",

        # 3. Divisão
        "Quanto é 100 dividido por 3?",

        # 4. Números Negativos
        "Quanto é 10 - 200?",

        # 5. Mistura de operações
        "Quanto é 100 * 2 + 50?",

        # 6. Raiz Quadrada 
        "Qual a raiz quadrada de 81?"
    ]

    print("🤖 INICIANDO BATERIA DE TESTES MATEMÁTICOS...\n")

    for pergunta in testes:
        print(f"❓ Pergunta: {pergunta}")
        try:
            payload = {"message": pergunta}
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                resposta_ia = response.json().get("response")
                print(f"💡 Resposta IA: {resposta_ia}")
            else:
                print(f"❌ Erro na API: {response.status_code}")

        except Exception as e:
            print(f"❌ Falha na conexão: {e}")

        print("-" * 30)


if __name__ == "__main__":
    testar_calculadora()
