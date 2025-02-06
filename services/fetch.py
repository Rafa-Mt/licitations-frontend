from services.supabase_client import supabase
import os
import time
import streamlit as st

def register(email: str, password: str) -> str:
    try:
        print("ASD")
        register_response = supabase.auth.sign_up({"email": email, "password": password})
        print("FGH")
        print(register_response)
        user_id = register_response.user.id
        rpc_response = supabase.rpc("insert_user_role", {"p_user_id": user_id}).execute()
        print(rpc_response)
        
        return register_response.session.access_token
    except Exception as e:
        print(e)

def login(email: str, password: str) -> tuple[str, str]:
    response = supabase.auth.sign_in_with_password({"email": email, "password": password})
    user_id = response.user.id
    print(user_id)
    user_type = supabase.table("user_role") \
        .select("role_id, role(description)") \
        .eq("user_id", user_id) \
        .execute() \
        .data[0]["role"]["description"]
    
    print(user_type)
    return (user_type, response.session.access_token)


def logout():
    supabase.auth.sign_out()
    st.session_state.popitem("key")


def send(encrypted_file, file_title, file_description, aes_key):
    try:
        dir_name = f'files/{file_title}-' + str(time.time())
        os.mkdir(dir_name)
        with open(f'files/{dir_name}/licitation', 'wb') as f:
            f.write(encrypted_file)
        with open(f'files/{dir_name}/key', 'w') as f:
            f.write(aes_key)

        result = supabase.table('application').insert([
            { 'title': file_title, 'description': file_description, 'dir': dir_name, 'state_id': 1 }
        ]).execute()
        
        if result.get('error'):
            raise Exception(result.get('error'))
        return True
    except Exception as e:
        print(e)
        return False


# get all the licitations
def get_licitations():
    result = supabase.table('application').select().execute()
    return result.get('data')


