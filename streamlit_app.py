import streamlit as st
import requests
import datetime

BASE_URL = "http://localhost:8000"  # Your FastAPI or Flask backend endpoint

st.set_page_config(
    page_title="☕ ZUS Coffee Agentic Chatbot",
    page_icon="☕",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("☕ ZUS Coffee Agentic Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.header("Ask anything about ZUS products, outlets, or promotions!")

# Chat input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="e.g. What tumblers are available?")
    submit_button = st.form_submit_button("Send")

# Handle user query
if submit_button and user_input.strip():
    try:
        with st.spinner("ZUSBot is thinking..."):
            payload = {"question": user_input}
            response = requests.post(f"{BASE_URL}/query", json=payload)

        if response.status_code == 200:
            answer = response.json().get("answer", "Sorry, no answer returned.")
            timestamp = datetime.datetime.now().strftime("%H:%M")

            # Append to history
            st.session_state.chat_history.append(("You", user_input, timestamp))
            st.session_state.chat_history.append(("ZUSBot", answer, timestamp))
        else:
            st.error(f"ZUSBot failed to respond: {response.text}")
    except Exception as e:
        st.error(f"Something went wrong: {e}")

# Display chat history
for sender, msg, time in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 You ({time}):** {msg}")
    else:
        st.markdown(f"**🤖 ZUSBot ({time}):** {msg}")
