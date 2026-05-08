import secrets
import hashlib

def hash_blake2s(message: str, salt_bytes: int = 32) -> tuple:
    """Blake2s Hash Function with salt"""
    salt = secrets.token_bytes(salt_bytes)
    hash_result = hashlib.blake2s(message.encode() + salt).hexdigest()
    return hash_result, salt.hex()
