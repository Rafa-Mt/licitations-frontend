import streamlit as st

@st.dialog("Send your licitation")
def send_modal():
    name = st.text_input("Licitation Name")
    description = st.text_area("Licitation Description")

    encrypted = st.file_uploader("Encrypted File")
    aes_key = st.file_uploader("AES Key")

    if st.button("Send application", use_container_width=True):
        st.rerun()
