import streamlit as st

@st.dialog("Approve or reject licitation")
def approve_dialog():
    option = st.selectbox(
        "Set state",
        ("Approved", "Rejected")
    )

    if st.button("Send state", use_container_width = True):
        st.rerun()