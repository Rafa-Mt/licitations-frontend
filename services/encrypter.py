import subprocess
import os

def decrypt_file(filepath: str, key_path: str) -> bytes:
    filepath = os.path.abspath(filepath)
    key_path = os.path.abspath(key_path)
    private_key_path = os.path.abspath("./keys/private.pem")

    # Verifica que los archivos existen
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"El archivo {filepath} no se encontró.")
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"El archivo {key_path} no se encontró.")
    if not os.path.exists(private_key_path):
        raise FileNotFoundError(f"El archivo {private_key_path} no se encontró.")

    print("executing decrypt_file")
    # Ejecuta el comando de decriptación
    command = f".\\services\\encrypter.exe -d \"{filepath}\" \"{private_key_path}\" \"{key_path}\""
    result = os.system(command)


    out_file = "out.txt"

    if not os.path.exists(out_file):
        raise Exception("El archivo out.txt no se encontró después de la ejecución.")
    
    with open(out_file, "rb") as f:
        file_data = f.read()
    
    os.remove(out_file)
    
    return file_data
