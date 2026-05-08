import hashlib
import secrets

def hash_sha256(message: str, salt_bytes: int = 32) -> tuple:
    """SHA-256 Hash Function with salt"""
    salt = secrets.token_bytes(salt_bytes)
    hash_result = hashlib.sha256(message.encode() + salt).hexdigest()
    return hash_result, salt.hex()
