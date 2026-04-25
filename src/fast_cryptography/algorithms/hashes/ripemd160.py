import secrets
from Crypto.Hash import RIPEMD160

def hash_ripemd160(message: str, byte: int) -> str:
    """Ripemd160 Hash Function"""
    salt = secrets.token_bytes(byte)
    hash_obj = RIPEMD160.new()
    hash_obj.update(salt + message.encode())
    hash_result = hash_obj.hexdigest()

    return hash_result
    