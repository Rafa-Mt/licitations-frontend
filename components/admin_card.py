import streamlit as st
from components.approve_dialog import approve_dialog
from services.encrypter import decrypt_file
import os 


def admin_card(name: str, description: str, filepath: str, key_path: str):
    container = st.container()

    container.header(name)
    left, center, right = container.columns([0.7, 0.2, 0.1])
    left.subheader(description)
    center.button("Change State", on_click=approve_dialog, key=f"{name}-{description}-set")

    if right.button("Decrypt",on_click=  key=f"{name}-{description}-download"):
        try:
            print("aaaaaaaaaaaaaa")
            decrypted_data = decrypt_file(filepath, key_path)
            right.download_button(
                "",
                data=decrypted_data,
                file_name="out.txt",
                icon=":material/download_2:",
                key=f"{name}-{description}-download-final"
            )
        except Exception as error:
            st.error(f"Error al procesar la descarga: {error}")

    