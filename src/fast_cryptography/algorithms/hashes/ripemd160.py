import secrets
from Crypto.Hash import RIPEMD160

def hash_ripemd160(message: str, salt_len: int = 32) -> tuple:
    """RIPEMD160 Hash Function with salt"""
    salt = secrets.token_bytes(salt_len)
    hash_obj = RIPEMD160.new()
    hash_obj.update(salt + message.encode())
    hash_result = hash_obj.hexdigest()
    return hash_result, salt.hex()