import streamlit as st

if "msgs" not in st.session_state:
    st.session_state["msgs"] = []