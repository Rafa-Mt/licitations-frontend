from supabase import create_client, Client
from supabase.client import ClientOptions
import streamlit as st

KEY = st.secrets["supabase"]["key"]
URL = st.secrets["supabase"]["url"]

try:
    supabase: Client = create_client(URL, KEY,
      options=ClientOptions(
        postgrest_client_timeout=10,
        storage_client_timeout=10,
        schema="public",
      )
    )
except Exception as e:
    st.toast("Error connecting to the server")
    st.error(f"Connection error: {e}")