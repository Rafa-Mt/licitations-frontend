import streamlit as st
from components.approve_dialog import approve_dialog
def admin_card(name: str, description: str):
    container = st.container(border=True)

    container.header(name)
    left, center, right = container.columns([0.7, 0.2, 0.1])
    left.subheader(description)

    center.button("Change State", on_click=approve_dialog, key=f"{name}-{description}-set")
    right.download_button("", data="aa", icon=":material/download_2:", key=f"{name}-{description}-download")