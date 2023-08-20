import streamlit as st

for msg in st.session_state["msgs"]:
    st.chat_message(msg["role"]).write(msg["content"]) 

if prompt := st.chat_input(placeholder="enter message"):
    st.session_state["msgs"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

