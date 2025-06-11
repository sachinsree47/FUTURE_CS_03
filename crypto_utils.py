from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

KEY = b'MyUltraSecretAES256KeyForTesting'

def encrypt_file(data):
    iv = get_random_bytes(16)  
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    return iv + encrypted_data  

def decrypt_file(encrypted_data):
    iv = encrypted_data[:16]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size)
    return decrypted_data
