import streamlit as st

cookies = st.context.cookies

if cookies.get("token"):
    st.navigation("main")

st.write("aisdoa")

load_cookies = st.button("Load cookies")
if load_cookies:
    pass