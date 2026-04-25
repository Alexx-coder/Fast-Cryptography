import hashlib
import secrets

def hash_md5(message: str, byte: int) -> str:
    """MD5 Hash Function"""
    salt = secrets.token_bytes(byte)
    return hashlib.md5(message + salt.encode()).hexdigest()
    