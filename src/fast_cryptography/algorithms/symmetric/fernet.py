from cryptography.fernet import Fernet

def generate_key() -> str:
    """Generates a new Fernet key"""
    key = Fernet.generate_key()
    return key.decode('utf-8')

def encrypt(message: str, key: str) -> str:
    """Encrypts a message using Fernet key"""
    cipher = Fernet(key.encode())
    encrypted = cipher.encrypt(message.encode())
    return encrypted.decode('utf-8')


def decrypt(encrypted: str, key: str) -> str:
    """Decrypts a message using Fernet key"""
    cipher = Fernet(key.encode())
    decrypted = cipher.decrypt(encrypted.encode())
    return decrypted.decode('utf-8')
