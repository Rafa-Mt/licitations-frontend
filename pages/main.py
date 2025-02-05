import streamlit as st
from components.card import card

cards = {
    "lict1": "approved",
    "lict2": "rejected",
    "lict3": "pending"
}

for title, state in cards.items():
    card(title, "Asdasd", state)