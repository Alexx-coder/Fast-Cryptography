import secrets
import hashlib

def hash_blake2b(message: str, salt_bytes: int = 32) -> tuple:
    """Blake2b Hash Function with salt"""
    salt = secrets.token_bytes(salt_bytes)
    hash_result = hashlib.blake2b(message.encode() + salt).hexdigest()
    return hash_result, salt.hex()
    