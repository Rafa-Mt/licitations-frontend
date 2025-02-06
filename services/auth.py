import streamlit as st
import services.fetch as fetch
from supabase import AuthApiError,AuthRetryableError

def login(email: str, password: str) -> None:
    try:
        user_type, token = fetch.login(email, password)
        st.session_state['token'] = token
        st.switch_page(f"./pages/{user_type}.py")
    except AuthApiError:
        st.error("Invalid Credentials")
    except AuthRetryableError:
        st.error("SSL handshake timed out. Please try again.")

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

def check_token():
    if 'token' not in st.session_state:
        st.switch_page("./login.py")
        st.toast("you need to login")
        return
    return

    


    

