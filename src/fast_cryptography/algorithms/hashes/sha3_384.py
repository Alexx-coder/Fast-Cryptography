import secrets
import hashlib

def hash_sha3_384(message: str, byte: int) -> str:
    """SHA3-384 Hash Function"""
    salt = secrets.token_bytes(byte)
    return hashlib.sha3_384(message + salt.encode()).hexdigest()

    