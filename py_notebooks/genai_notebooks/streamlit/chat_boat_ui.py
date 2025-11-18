import streamlit as st

# Set page configuration
st.set_page_config(page_title="TechConvos - Chart", page_icon="💬", layout="wide")

# Display main title
st.title("💬 TechConvos - Chart (Local)")

# Keep chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render chat history
for role, content in st.session_state.messages:
    with st.chat_message(role):
        st.markdown(content)

# Input box for user message
if prompt := st.chat_input("Type a message...."):
    # Store user message in session state
    st.session_state.messages.append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant reply
    reply = f"You Said: **{prompt}**"
    # Store assistant reply in session state
    st.session_state.messages.append(("assistant", reply))
    with st.chat_message("assistant"):
        st.markdown(reply)

