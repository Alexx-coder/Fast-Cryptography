import hashlib
import secrets

def hash_sha256(message: str, byte: int) -> str:
    """SHA-256 Hash Function"""
    salt = secrets.token_bytes(byte)
    return hashlib.sha256(message + salt.encode()).hexdigest()


