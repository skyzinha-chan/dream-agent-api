# Se a biblioteca strands_agents não for encontrada, me avise!
# Estou usando uma estrutura genérica compatível com requests/ollama para garantir funcionalidade
# caso o SDK tenha sintaxe específica que não conhecemos.

import requests
import json
from app.core.config import settings
from app.agent.tools import calculate_tool


class DreamAgent:
    def __init__(self):
        self.model = settings.OLLAMA_MODEL
        self.api_url = f"{settings.OLLAMA_BASE_URL}/api/generate"

        # Prompt de Sistema: Ensina o Agente quem ele é e como usar ferramentas
        # Prompt de Sistema Refinado
        self.system_prompt = """
        Você é um assistente preciso da DreamSquad.
        
        FERRAMENTA DE CÁLCULO:
        Se o usuário pedir QUALQUER conta matemática, você DEVE responder APENAS neste formato:
        CALC: [expressão matemática]
        
        Exemplos Corretos:
        Usuário: Quanto é 2 + 2?
        Você: CALC: 2 + 2
        
        Usuário: Raiz de 144
        Você: CALC: math.sqrt(144)
        
        Usuário: 50 vezes 2
        Você: CALC: 50 * 2

        REGRA DE OURO:
        - NÃO explique o cálculo antes.
        - NÃO invente continuação de conversa.
        - Se receber o resultado da tool, apenas diga o número final ou uma frase curta.
        """

    def process_message(self, user_message: str) -> str:
        """
        Processa a mensagem, verifica se precisa usar ferramenta e retorna a resposta final.
        """
        # 1. Pergunta inicial para a LLM
        full_prompt = f"{self.system_prompt}\n\nUsuário: {user_message}\nAssitente:"

        response_text = self._call_ollama(full_prompt)

        # 2. Verifica se a IA pediu para usar a calculadora (Pattern Matching)
        if "CALC:" in response_text:
            # Extrai a conta (ex: "CALC: 123 * 4") -> "123 * 4"
            expression = response_text.split("CALC:")[1].strip()
            print(f"🧮 Agente solicitou cálculo: {expression}")

            # Usa a Tool que criamos na Etapa 3
            result = calculate_tool(expression)

            # 3. Devolve o resultado para a IA formular a resposta final
            final_prompt = f"{full_prompt}\n{response_text}\nSistema (Resultado da Tool): {result}\nAssitente (responda o usuário com o resultado):"
            final_response = self._call_ollama(final_prompt)
            return final_response

        return response_text

    def _call_ollama(self, prompt: str) -> str:
        """Função auxiliar para chamar a API do Ollama"""
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        try:
            response = requests.post(self.api_url, json=payload)
            response.raise_for_status()
            return response.json().get("response", "")
        except Exception as e:
            return f"Erro na comunicação com IA: {e}"


# Instância global do agente
agent = DreamAgent()
