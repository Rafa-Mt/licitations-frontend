import streamlit as st
# from services.fetch import login as fetch_login, register as fetch_register, session
from supabase import Client, AuthApiError

def login(email: str, password: str, client: Client) -> bool:
    try:
        response = client.auth.sign_in_with_password({"email": email, "password": password})
        save_token(response.session.access_token)
        user_id = response.user.id
        print(user_id)
        user_type = client.table("user_role") \
            .select("role_id, role(description)") \
            .eq("user_id", user_id) \
            .execute() \
            .data[0]["role"]["description"]
        
        print(user_type)

        return True
    except AuthApiError:
        st.error("Invalid Credentials")
        return False


def register(username: str, email: str, password: str, client: Client) -> bool:
    try:
        response = client.auth.sign_up({"email": email, "password": password})
        save_token(response.session.access_token)
        return True
    except AuthApiError:
        st.error("Invalid Credentials")
        return False


def save_token(token):
    st.session_state['token'] = token