import secrets
import hashlib

def hash_sha3_384(message: str, salt_bytes: int = 32) -> tuple:
    """SHA3-384 Hash Function with salt"""
    salt = secrets.token_bytes(salt_bytes)
    hash_result = hashlib.sha3_384(message.encode() + salt).hexdigest()
    return hash_result, salt.hex()