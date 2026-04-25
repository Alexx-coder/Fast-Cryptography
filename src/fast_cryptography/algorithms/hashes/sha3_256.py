import secrets
import hashlib

def hash_sha3_256(message: str, byte: int) -> str:
    """SHA3-256 Hash Function"""
    salt = secrets.token_bytes(byte)
    return hashlib.sha3_256(message + salt.encode()).hexdigest()