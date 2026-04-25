import secrets
import hashlib

def hash_sha3_224(message: str, byte: int) -> str:
    """SHA3-224 Hash Function"""
    salt = secrets.token_bytes(byte)
    return hashlib.sha3_224(message + salt.encode()).hexdigest()
