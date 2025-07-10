import streamlit as st
import datetime
import os
from agent.workflow import GraphBuilder

# Cache the LangGraph once
@st.cache_resource
def load_react_app():
    graph = GraphBuilder(model_provider="openai")
    return graph()

react_app = load_react_app()

st.set_page_config(
    page_title="☕ ZUS Coffee Agentic Chatbot",
    page_icon="☕",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("☕ ZUS Coffee Agentic Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.header("Ask anything about ZUS products, outlets, or promotions!")

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("You:", placeholder="e.g. What tumblers are available?")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input.strip():
    try:
        with st.spinner("ZUSBot is thinking..."):
            output = react_app.invoke({"messages": [user_input]})

            if isinstance(output, dict) and "messages" in output:
                final_output = output["messages"][-1].content
            else:
                final_output = str(output)

            timestamp = datetime.datetime.now().strftime("%H:%M")
            st.session_state.chat_history.append(("You", user_input, timestamp))
            st.session_state.chat_history.append(("ZUSBot", final_output, timestamp))

    except Exception as e:
        st.error(f"Something went wrong: {e}")

# Display chat history
for sender, msg, time in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑 You ({time}):** {msg}")
    else:
        st.markdown(f"**🤖 ZUSBot ({time}):** {msg}")
