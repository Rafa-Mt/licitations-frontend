import streamlit as st
from services.encrypter import decrypt_file

@st.dialog('download')
def download_dialog(filepath: str, key_path: str, name: str, description: str):
    try:
        st.write("Are you sure you want to download this file?")
        decrypted_data = decrypt_file(filepath, key_path)
        st.download_button(
            "Download file",
            data=decrypted_data,
            file_name="out.txt",
            icon=":material/download_2:",
            key=f"{name}-{description}-download-final",
            use_container_width=True
        )
    except Exception as error:
        st.error(f"Error al procesar la descarga: {error}")