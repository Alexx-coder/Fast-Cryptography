import secrets
import hashlib

def hash_blake2b(message: str, byte: int) -> str:
    """Blake2b Hash Function"""
    salt = secrets.token_bytes(byte)
    return hashlib.blake2b(message + salt.encode()).hexdigest()
    