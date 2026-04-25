import secrets
import hashlib

def hash_blake2s(message: str, byte: int) -> str:
    """Blake2s Hash Function"""
    salt = secrets.token_bytes(byte)
    return hashlib.blake2s(message + salt.encode()).hexdigest()

    