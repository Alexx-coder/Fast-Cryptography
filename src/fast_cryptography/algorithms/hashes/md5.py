import hashlib
import secrets

def hash_md5(message: str, salt_bytes: int = 32) -> tuple:
    """MD5 Hash Function with salt"""
    salt = secrets.token_bytes(salt_bytes)
    hash_result = hashlib.md5(message.encode() + salt).hexdigest()
    return hash_result, salt.hex()