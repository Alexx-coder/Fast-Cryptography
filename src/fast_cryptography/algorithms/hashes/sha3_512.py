import secrets
import hashlib

def hash_sha3_512(message: str, salt_bytes: int = 32) -> tuple:
    """SHA3-512 Hash Function with salt"""
    salt = secrets.token_bytes(salt_bytes)
    hash_result = hashlib.sha3_512(message.encode() + salt).hexdigest()
    return hash_result, salt.hex()