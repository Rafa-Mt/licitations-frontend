import streamlit as st
from components.admin_card import admin_card
from services.supabase_client import supabase
from services.fetch import get_licitations
from services.auth import check_token

check_token()
st.header("Admin's Licitations")



licitations = get_licitations()





cards = {
    "lict1": "approved",
    "lict2": "rejected",
    "lict3": "pending"
}

for item in licitations:
    #print(f"{item['id']}\n")
    admin_card(item['id'],item['title'], item['description'], item['file_dir'], item['aes_key_dir'])
