from Crypto.Hash import MD4
import secrets

def hash_md4(message: str, byte: int) -> str:
    """MD4 Hash Function"""
    salt = secrets.token_bytes(byte)
    hash_obj = MD4.new()
    hash_obj.update(salt + message.encode())
    hash_result = hash_obj.hexdigest()
    return hash_result