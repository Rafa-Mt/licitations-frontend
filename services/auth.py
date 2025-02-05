import streamlit as st

def login(username: str, password: str) -> bool:
    st.toast("Logged in")
    st.switch_page("./pages/main.py")

def register(username: str, email: str, password: str) -> bool:
    st.toast('Registered')

def save_token(token):
    st.session_state['token'] = token
    