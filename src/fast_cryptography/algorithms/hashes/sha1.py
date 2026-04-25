import secrets
import hashlib

def hash_sha1(message: str, byte: int) -> str:
    """SHA-1 Hash Function"""
    salt = secrets.token_bytes(byte)
    return hashlib.sha1(message + salt.encode()).hexdigest()
    