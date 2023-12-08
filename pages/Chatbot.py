# Import necessary  libraries

import streamlit as st

from sphere.chat_manager import main as chat_manager

st.set_page_config(page_title=" Optim Assistant", layout="wide")


st.title("Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "Agent", "content": "Hello"}]

# display the messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# add a chat input
if user_message := st.chat_input():
    # add the user message to the session state
    st.session_state.messages.append({"role": "Patient", "content": user_message})
    st.chat_message("user").write(user_message)
    conversation = " "  # initialize the conversation string
    for msg in st.session_state.messages:
        # add the role and content of each message to the conversation string
        conversation += "\n\n\n" + msg["role"] + ": " + msg["content"]
    # get the response from the chat manager
    response = chat_manager(user_message)
    st.session_state.messages.append({"role": "Agent", "content": response})
    st.chat_message("assistant").markdown(response)
