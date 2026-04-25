import base58 as b58

def encode(data: bytes) -> str:
    """Encode using module base58"""
    return b58.b58encode(data).decode()

def decode(data: str) -> bytes:
    """Decode using module base58"""
    return b58.b58decode(data)

def is_valid(data: str) -> bool:
    """Check if string is base58"""
    try:
        bytes.fromhex(data)
        return True
    except:
        return False    