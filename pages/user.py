import streamlit as st
from components.card import card
from components.send_dialog import send_modal

cards = {
    "lict1": "approved",
    "lict2": "rejected",
    "lict3": "pending"
}

left, right = st.columns(2)

if left.button("Get Encryption Key", use_container_width=True):
    pass

if right.button("Send Licitation", use_container_width=True):
    send_modal()

for title, state in cards.items():
    card(title, "Asdasd", state)

if len(cards) == 0:
    st.subheader("You don't have any licitation... Create one.")