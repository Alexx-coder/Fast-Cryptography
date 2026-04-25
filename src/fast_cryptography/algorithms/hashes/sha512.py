import secrets
import hashlib

def hash_sha512(message: str, byte: int) -> str:
    """SHA-512 Hash Function"""
    salt = secrets.token_bytes(byte)
    return hashlib.sha512(message + salt.encode()).hexdigest()
