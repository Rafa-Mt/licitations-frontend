import streamlit as st
from services.actions import call_return

def on_button_click():
    out = call_return("python", "./pages/test.py")
    st.toast(out)

st.button("Execute", on_click=on_button_click)