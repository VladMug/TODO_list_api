from cryptography.fernet import Fernet
from config.config import ENCODER_KEY

f = Fernet(ENCODER_KEY)

def encode_note(note:str) -> str: 
    encrypted_note = f.encrypt(bytes(note, encoding = 'utf-8'))
    return encrypted_note

def decode_note(note:str) -> str:
    decrypted_note = f.decrypt(bytes(note)).decode('utf-8')
    return decrypted_note