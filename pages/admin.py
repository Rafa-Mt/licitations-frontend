import streamlit as st
from components.admin_card import admin_card

cards = {
    "lict1": "approved",
    "lict2": "rejected",
    "lict3": "pending"
}

for title, state in cards.items():
    admin_card(title, "Asdasd"*32)