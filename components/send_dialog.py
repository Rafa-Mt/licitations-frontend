import streamlit as st
import services.fetch as fetch 

@st.dialog("Send your licitation")
def send_modal():
    with st.form("sender", border=False):
        title = st.text_input("Licitation Title")
        description = st.text_area("Licitation Description")

        encrypted_file = st.file_uploader("Encrypted File")
        aes_key_file = st.file_uploader("AES Key")

        if st.form_submit_button("Send application", use_container_width=True, type='primary'):
            if all([title, description, encrypted_file, aes_key_file]):
                fetch.send(encrypted_file, title, description, aes_key_file)
                st.rerun()
                st.toast("Licitation sended successfully")
            else:
                st.error("Please fill out all fields")
