import streamlit as st
import services.auth as auth

cookies = st.context.cookies

if cookies.get("token"):
    st.navigation("main")

st.session_state.sidebar_visible = False

login, register = st.tabs(["Login", "Register"])

with login:
    with st.form(key="login") as form:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Login"): 
            if auth.login(username, password): 
                st.switch_page("./pages/main.py")
            else:
                st.error("Invalid username or password")

with register:
    with st.form(key="register") as form:
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.form_submit_button("Register"):
            if auth.register(username, email, password):
                st.switch_page("./pages/main.py")
            else:
                st.error("Failed to register, please try again later")