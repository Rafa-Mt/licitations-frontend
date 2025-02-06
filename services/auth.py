import streamlit as st
import services.fetch as fetch
from supabase import AuthApiError
from services.supabase_client import supabase

def login(email: str, password: str) -> None:
    try:
        user_type, token = fetch.login(email, password)
        st.session_state['token'] = token
        st.switch_page(f"./pages/{user_type}.py")
    except AuthApiError:
        st.error("Invalid Credentials")

def register(email: str, password: str) -> None:
    try:
        print('registers before')
        token = fetch.register(email, password)
        print('registers after')
        st.session_state['token'] = token
        st.switch_page("./pages/user.py")
        return True
    except AuthApiError:
        st.error("Invalid Credentials")
        return False


def save_token(token):
    st.session_state['token'] = token