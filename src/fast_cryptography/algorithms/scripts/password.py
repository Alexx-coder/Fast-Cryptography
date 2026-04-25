from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import secrets
import base64

def auth(pwd: str, salt: bytes = None) -> tuple:
    """Hash a password with PBKDF2HMAC and SHA256"""
    if salt is None:
        salt = secrets.token_bytes(32)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    hash_bytes = kdf.derive(pwd.encode())
    
    return base64.b64encode(hash_bytes).decode(), salt.hex()

def verify(pwd: str, stored_hash: str, stored_salt: str) -> bool:
    """Verify password hash with PBKDF2HMAC and SHA256"""
    salt = bytes.fromhex(stored_salt)
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    
    try:
        kdf.verify(pwd.encode(), base64.b64decode(stored_hash))
        return True
    except Exception:
        return False 