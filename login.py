import streamlit as st
import services.auth as auth
from supabase import create_client

cookies = st.context.cookies

if cookies.get("token"):
    st.switch_page("./pages/main.py")

st.session_state.sidebar_visible = False


# login, register = st.tabs(["Login", "Register"])

# with login:
st.subheader("Login")
with st.form(key="login") as form:
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.form_submit_button("Login"):
        auth.login(email, password) 

# with register:
#     with st.form(key="register") as form:
#         email = st.text_input("Email")
#         password = st.text_input("Password", type="password")
#         if st.form_submit_button("Register"):
#             auth.register(email, password)
            
# if st.button("[Debug] Go to main"):
#     st.switch_page("./pages/main.py")

# if st.button("[Debug] Go to admin"):
#     st.switch_page("./pages/admin.py")
