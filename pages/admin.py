import streamlit as st
from components.admin_card import admin_card
from services.supabase_client import supabase

st.header("Admin's Licitations")

cards = {
    "lict1": "approved",
    "lict2": "rejected",
    "lict3": "pending"
}


admin_card("title", "ayuda", "./file/licitacion/out.bin", "./file/licitacion/aeskey_encrypted.bin")
    