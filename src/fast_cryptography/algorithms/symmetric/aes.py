from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
import secrets
import base64


def generate_key(key_size) -> str:
    """
    Generates an AES key.
    key_size: 16 (AES-128), 24 (AES-192), or 32 (AES-256)
    """
    key = secrets.token_bytes(key_size)
    return base64.b64encode(key).decode()


def encrypt(message: str, key_b64: str) -> str:
    """Encrypts a message using AES-CBC"""
    key = base64.b64decode(key_b64)
    iv = secrets.token_bytes(16)
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    padder = PKCS7(128).padder()
    padded_data = padder.update(message.encode()) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    result = iv + ciphertext
    return base64.b64encode(result).decode()


def decrypt(encrypted_b64: str, key_b64: str) -> str:
    """Decrypts an AES-CBC encrypted message"""
    key = base64.b64decode(key_b64)
    data = base64.b64decode(encrypted_b64)
    
    iv = data[:16]
    ciphertext = data[16:]
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ciphertext) + decryptor.finalize()
    
    unpadder = PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()
    
    return plaintext.decode()