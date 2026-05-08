import base64 as b64

def encode(data: bytes) -> str:
    """Encode using module base64 for base16"""
    return b64.b16encode(data).decode()

def decode(data: str) -> bytes:
    """Decode using module base54 for base16"""
    return b64.b16decode(data)

def is_valid(data: str) -> bool:
    """Check if string is base64 for base16"""
    try:
        bytes.fromhex(data)
        return True
    except:
        return False 