import secrets
import hashlib

def hash_sha3_512(message: str, byte: int) -> str:
    """SHA3-512 Hash Function"""
    salt = secrets.token_bytes(byte)
    return hashlib.sha3_512(message + salt.encode()).hexdigest()

    