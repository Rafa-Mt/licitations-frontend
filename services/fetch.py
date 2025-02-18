from services.supabase_client import supabase
from supabase import AuthApiError
import os
import time
import streamlit as st
from supabase import AuthApiError,AuthRetryableError

def register(email: str, password: str) -> str:
    try:
        register_response = supabase.auth.sign_up({"email": email, "password": password})
        user_id = register_response.user.id
        supabase.rpc("insert_user_role", {"p_user_id": user_id}).execute()
        
        return register_response.session.access_token
    except Exception as e:
        print(e)

def login(email: str, password: str) -> tuple[str, str]:
    response = supabase.auth.sign_in_with_password({"email": email, "password": password})
    user_id = response.user.id
    try:
        user_type = supabase.table("user_role") \
            .select("role_id, role(description)") \
            .eq("user_id", user_id) \
            .execute() \
            .data[0]["role"]["description"]
        print(user_type)
        return (user_type, response.session.access_token)
    except:
        raise AuthApiError()

def get_user_type():
    
    user_id = supabase.auth.get_user(st.session_state['token']).user.id
    

    user_type = supabase.table("user_role")\
        .select("role_id")\
        .eq("user_id", user_id)\
        .execute() 
        
    print(f"resutl {user_type}")
    
    return(user_type)




def logout():
    supabase.auth.sign_out()
    st.session_state.popitem("token")


def send(encrypted_file, file_title, file_description, aes_key):
    try:
        dir_name = f'./files/{file_title}-' + str(time.time())
        os.mkdir(dir_name)
        file_dir = f'{dir_name}/licitation.bin' 
        with open(file_dir, 'wb') as f:
            f.write(encrypted_file.read())

        key_dir = f'{dir_name}/key.bin' 
        with open(key_dir, 'wb') as f:
            f.write(aes_key.read())

        user_id = supabase.auth.get_user(st.session_state['token']).user.id
        result = supabase.table('application').insert([{ 
            'title': file_title, 
            'description': file_description, 
            'file_dir': file_dir, 
            'aes_key_dir': key_dir, 
            'state_id': 1, 
            'user_id': user_id 
        }]).execute()
        
        if result['error']:
            os.rmdir(dir_name)
            raise Exception(result.get('error'))
        return True
    except Exception as e:
        print(e)
        return False

def get_user_licitations(user_id):
    try:
        result = supabase.table("application") \
            .select('*') \
            .filter('user_id', 'eq', user_id) \
            .execute()
        if result.status_code == 200:
            return result.data
        else:
            print(f"Failed to fetch licitations: {result}")
            return None
    except Exception as e:
        print(f"Error fetching licitations: {e}")
        return None


# get all the licitations
def get_licitations():
    try:
        result = supabase.table("application") \
            .select('id,title, description, file_dir, aes_key_dir') \
            .filter('state_id', 'eq', 1) \
            .execute()
        return result.data
    except AuthRetryableError:
        st.error("SSL handshake timed out. Please try again.")



def update_state(licitation_id, new_state):
    print("xxxx")
    user_type=get_user_type()
    
    print(f"user_type: {user_type}")



    result = supabase.table("application") \
        .update({'state_id': new_state}) \
        .filter('id', 'eq', licitation_id) \
        .execute()
    
        
        
    


