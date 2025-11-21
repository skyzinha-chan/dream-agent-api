from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    # Exemplo para documentação automática (Swagger UI)
    model_config = {
        "json_schema_extra": {
            "examples": [
                {"message": "Quanto é 1234 * 5678?"}
            ]
        }
    }


class ChatResponse(BaseModel):
    response: str
