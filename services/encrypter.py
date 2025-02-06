import subprocess
import os

def decrypt_file(filepath: str, key_path: str) -> bytes:
    print(f"decrypting {filepath}  {key_path}")
    os.system(f".\services\encrypter.exe -d {filepath} private.pem {key_path}")

    out_file = "out.txt"

    if not os.path.exists(out_file):
        raise Exception("El archivo out.txt no se encontró después de la ejecución.")
    
    with open(out_file, "rb") as f:
        file_data = f.read()
    
    os.remove(out_file)
    
    return file_data
