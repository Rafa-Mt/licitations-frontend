from supabase import create_client, Client
from supabase.client import ClientOptions
import streamlit as st

KEY = st.secrets["supabase"]["key"]
URL = st.secrets["supabase"]["url"]

supabase: Client = create_client(URL, KEY,
  options=ClientOptions(
    postgrest_client_timeout=10,
    storage_client_timeout=10,
    schema="public",
  ))
