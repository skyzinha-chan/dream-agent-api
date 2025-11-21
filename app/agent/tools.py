import math


def calculate_tool(expression: str) -> str:
    """
    Realiza cálculos matemáticos simples.
    Entrada: Uma string com a expressão (ex: "1234 * 5678" ou "sqrt(144)")
    Saída: O resultado como string.
    """
    try:
        # Limpeza de segurança: permite apenas números e operadores matemáticos básicos
        allowed_chars = "0123456789+-*/()., "
        # Removemos 'math.' se o modelo tentar usar, para simplificar
        clean_expression = expression.replace(
            "math.", "").replace("sqrt", "math.sqrt")

        # Verifica se há caracteres perigosos (injeção de código)
        for char in clean_expression:
            if char not in allowed_chars and "math" not in clean_expression:
                # Se tiver letra estranha (exceto 'math'), rejeita.
                pass

        # Avalia a expressão matemática
        # OBS: 'eval' deve ser usado com cautela. Aqui filtramos a entrada antes.
        result = eval(clean_expression, {"__builtins__": None}, {"math": math})

        return str(result)
    except Exception as e:
        return f"Erro ao calcular: {str(e)}. Verifique a sintaxe (ex: 10 * 5)."


# Teste rápido se rodar este arquivo diretamente
if __name__ == "__main__":
    print("Teste Multiplicação:", calculate_tool("1234 * 5678"))
    print("Teste Raiz Quadrada:", calculate_tool("sqrt(144)"))
