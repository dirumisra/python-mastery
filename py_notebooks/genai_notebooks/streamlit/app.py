import streamlit as st
from utils import get_openai_client

st.set_page_config(page_title = "TechConvos - LLM Chat",page_icon="🤖",layout="wide")
st.title("🤖 TechConvos - LLM Chat (OpenAI)")

# --- Sidebar controls ---
with st.sidebar:
    st.header("⚙️ Settings")
    model = st.selectbox("Model",["gpt-4o-mini","gpt-4o","gpt-4o-mini-translate"],index=0)
    temperature = st.slider('Temprature', 0.0,1.0,0.2,0.1)
    st.caption("Tip: lower temprature for factual, higher for creative.")
    st.divider()
    st.markdown("**Keys**: from `.env` locally or `.streamlit/secrets.toml` on cloud.")

# --- Session history ---
if "messages" not in st.session_state:
    st.session_state.message = [
        ("system", "You are TechConvosBot, concise and helpful.")
    ]

# --- Render past messages (skip system) ---
for role, content in st.session_state.message:
    if role == "system":
        continue
    with st.chat_message(role):
        st.markdown(content)

# --- Input + OpenAI call ---
if prompt := st.chat_input("Ask anything..."):
    #show user message
    st.session_state.message.append(("user",prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    client = get_openai_client()
    message = [{"role" : r,"content" : c} for r, c in st.session_state.message]

    # Stream the assistant reply token-by-token
    with st.chat_message("assistant"):
        stream_placeholder = st.empty()
        streamed_text = ""

        stream = client.chat.completion.create(
            model=model,
            message=message,
            temperature=temperature,
            stream=True
        )
        for chunk in stream:
            delta = chunk.choice[0].delta.content or ""
            streamed_text += delta
            stream_placeholder.markdown(streamed_text)

    st.session_state.message.append(("assistant",streamed_text))