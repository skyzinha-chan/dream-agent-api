import streamlit as st
import requests

# Configuração da Página
st.set_page_config(
    page_title="Dream Agent Chat",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Dream Agent & Math Tool")
st.markdown("---")

# Inicializa o histórico do chat se não existir
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens antigas
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada do usuário
if prompt := st.chat_input("Digite sua mensagem ou cálculo..."):
    # 1. Mostra a mensagem do usuário na tela
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Chama a sua API (Backend)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")

        try:
            # Conecta na API local
            response = requests.post(
                "http://localhost:8000/chat",
                json={"message": prompt}
            )

            if response.status_code == 200:
                ai_response = response.json().get("response")
                message_placeholder.markdown(ai_response)
                # Salva a resposta no histórico
                st.session_state.messages.append(
                    {"role": "assistant", "content": ai_response})
            else:
                message_placeholder.error(
                    f"Erro na API: {response.status_code}")

        except Exception as e:
            message_placeholder.error(
                f"Erro de conexão: Verifique se a API está rodando! \n\nDetalhe: {e}")
