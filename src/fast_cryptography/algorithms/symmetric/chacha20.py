from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from cryptography.hazmat.backends import default_backend
import secrets
import base64


def generate_key() -> str:
    """Generates a ChaCha20 key (32 bytes)"""
    key = secrets.token_bytes(32)
    return base64.b64encode(key).decode()


def encrypt(message: str, key_b64: str) -> str:
    """Encrypts a message using ChaCha20"""
    key = base64.b64decode(key_b64)
    nonce = secrets.token_bytes(16)
    
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
    
    result = nonce + ciphertext
    return base64.b64encode(result).decode()


def decrypt(encrypted_b64: str, key_b64: str) -> str:
    """Decrypts a ChaCha20 encrypted message"""
    key = base64.b64decode(key_b64)
    data = base64.b64decode(encrypted_b64)
    
    nonce = data[:16]
    ciphertext = data[16:]
    
    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
    return plaintext.decode()