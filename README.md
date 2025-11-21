dream-agent-api/
├── app/
│   ├── __init__.py
│   ├── main.py             # Ponto de entrada da aplicação (FastAPI app)
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py       # Definição do endpoint /chat
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py       # Carregamento de variáveis de ambiente (.env)
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── engine.py       # Configuração do Agente Strands e conexão com Ollama
│   │   └── tools.py        # A lógica da Tool de Cálculo Matemático
│   └── schemas/
│       ├── __init__.py
│       └── chat.py         # Modelos Pydantic (Input/Output JSON)
├── .env                    # Chaves e configurações (NÃO SOBE PRO GIT)
├── .gitignore              # Arquivos ignorados 
├── requirements.txt        # Dependências do projeto 
└── README.md               # Instruções de uso