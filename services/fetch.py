import requests
import streamlit as st

BASE_URL = st.secrets["backend_url"]
session = requests.Session()

def auth_register(username, password, email):
    url = f"{BASE_URL}/auth/register"
    payload = {
        "username": username,
        "password": password,
        "email": email
    }
    response = session.post(url, json=payload)
    return response.json()

def auth_login(username, password):
    url = f"{BASE_URL}/auth/login"
    payload = {
        "username": username,
        "password": password
    }
    response = session.post(url, json=payload)
    return response.json()

def auth_logout():
    url = f"{BASE_URL}/auth/logout"
    response = session.post(url)
    return response.json()

def send_text(text, aes_key_path=None, application_path=None):
    url = f"{BASE_URL}/send/text"
    data = {"text": text}
    files = {}

    if aes_key_path:
        files["aes_key"] = open(aes_key_path, 'rb')
    if application_path:
        files["application"] = open(application_path, 'rb')

    response = session.post(url, data=data, files=files)
    

    for file in files.values():
        file.close()
    
    return response.json()

def get_applications():
    url = f"{BASE_URL}/application/"
    response = session.get(url)
    return response.json()