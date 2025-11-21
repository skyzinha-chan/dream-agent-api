from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.agent.engine import agent  # Importamos o agente que criamos ontem

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Recebe uma mensagem do usuário e retorna a resposta da IA.
    O Agente decide automaticamente se usa a calculadora ou conversa normal.
    """
    try:
        print(f"📩 Recebido: {request.message}")

        # Chama o nosso Agente Inteligente
        ai_response = agent.process_message(request.message)

        return ChatResponse(response=ai_response)

    except Exception as e:
        # Se der erro, retorna código 500 (Erro Interno)
        print(f"❌ Erro no processamento: {e}")
        raise HTTPException(status_code=500, detail=str(e))
# Nota: Lembre-se de registrar esta rota no main.py para que fique ativa!