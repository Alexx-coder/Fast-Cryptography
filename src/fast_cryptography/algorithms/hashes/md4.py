from Crypto.Hash import MD4
import secrets

def hash_md4(message: str, salt_bytes: int = 32) -> tuple:
    """MD4 Hash Function with salt"""
    salt = secrets.token_bytes(salt_bytes)
    hash_obj = MD4.new()
    hash_obj.update(salt + message.encode())
    hash_result = hash_obj.hexdigest()
    return hash_result, salt.hex()
