import streamlit as st
from components.approve_dialog import approve_dialog
from components.download_dialog import download_dialog
from services.encrypter import decrypt_file
import random

def admin_card(id,name: str, description: str, filepath: str, key_path: str):
    container = st.container(border=True)
    container.header(name)
    
    left, center, right = container.columns([0.7, 0.2, 0.1])
    left.subheader(description)
    center.button("Change State", on_click=lambda: approve_dialog(id), key=f"{id}-{description}-set-{random.randint(0, 100)}")

    def download_file():    
        download_dialog(filepath, key_path, name, description)
        
    right.button("", icon=':material/download_2:', on_click=download_file,key=f"{name}-{description}-download-{random.randint(0, 100)}")


       

    