import streamlit as st
from components.card import card
from components.send_dialog import send_modal
from services.auth import check_token

check_token()


cards = {
    "lict1": "approved",
    "lict2": "rejected",
    "lict3": "pending"
}

left, right = st.columns(2)

with open("./keys/public.pem", "+r") as key:
    left.download_button(
        "Get Encryption Key", 
        data=key, 
        use_container_width=True,
        file_name="public.pem",
        mime="application/octet-stream"
    )
    

if right.button("Send Licitation", use_container_width=True):
    send_modal()

for title, state in cards.items():
    card(title, "Asdasd", state)

if len(cards) == 0:
    st.subheader("You don't have any licitation... Create one.")