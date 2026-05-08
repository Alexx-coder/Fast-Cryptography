import secrets
import hashlib

def hash_sha1(message: str, salt_bytes: int = 32) -> tuple:
    """SHA-1 Hash Function with salt"""
    salt = secrets.token_bytes(salt_bytes)
    hash_result = hashlib.sha1(message.encode() + salt).hexdigest()
    return hash_result, salt.hex()