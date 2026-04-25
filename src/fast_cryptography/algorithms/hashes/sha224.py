import secrets
import hashlib

def hash_sha224(message: str, byte: int) -> str:
    """SHA-224 Hash Function"""
    salt = secrets.token_bytes(byte)
    return hashlib.sha224(message + salt.encode()).hexdigest()

    