import streamlit as st
from components.approve_dialog import approve_dialog
from components.download_dialog import download_dialog
from services.encrypter import decrypt_file

def admin_card(name: str, description: str, filepath: str, key_path: str):
    container = st.container()

    container.header(name)
    left, center, right = container.columns([0.7, 0.2, 0.1])
    left.subheader(description)
    center.button("Change State", on_click=approve_dialog, key=f"{name}-{description}-set")

    if right.button("Decrypt", key=f"{name}-{description}-download"):
        download_dialog(filepath, key_path, name, description)
       

    