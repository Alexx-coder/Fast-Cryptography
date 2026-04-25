import secrets
import hashlib

def hash_sha384(message: str, byte: int) -> str:
    """SHA-384 Hash Function"""
    salt = secrets.token_bytes(byte)
    return hashlib.sha384(message + salt.encode()).hexdigest()
    