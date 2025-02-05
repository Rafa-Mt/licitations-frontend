import streamlit as st
from fetch import login as fetch_login, register as fetch_register,session

def login(username: str, password: str) -> bool:
    response = fetch_login(username, password)
    if response.get("message") == "Login exitoso":
        token = session.cookies.get("token")
        if token:
            save_token(token)
            st.toast("Logged in")
            st.switch_page("./pages/main.py")
            return True
    st.error("Login failed")
    return False

def register(username: str, email: str, password: str) -> bool:
    response = fetch_register(username, password, email)
    if response.get("mensaje") == "Usuario registrado correctamente":
        st.toast("Registered")
        return True
    else:
        st.error("Registration failed")
        return False

def save_token(token):
    st.session_state['token'] = token