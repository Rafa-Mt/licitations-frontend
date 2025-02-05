from supabase_client import supabase
import os
import time

def register(email, password):
    supabase.auth.sign_up(email=email, password=password)


def login(email, password):
    supabase.auth.sign_in(email=email, password=password)



def logout():
    supabase.auth.sign_out()

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


