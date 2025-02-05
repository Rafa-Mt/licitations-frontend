import streamlit as st

def card(name: str):
    container = st.container()
    
    container.subheader(name)

    return container
