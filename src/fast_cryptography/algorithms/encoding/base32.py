import base64 as b64

def encode(data: bytes) -> str:
    """Encode using module base64 for base32"""
    return b64.b32encode(data).decode()

def decode(data: str) -> bytes:
    """Decode using module base64 for base32"""
    return b64.b32decode(data)

def is_valid(data: str) -> bool:
    """Check if string is base64 fror base32"""
    try:
        bytes.fromhex(data)
        return True
    except:
        return False