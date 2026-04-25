import base64 as b64

def encode(data: bytes) -> str:
    """Encode using module base64 for base85"""
    return b64.b85encode(data).decode()

def decode(data: str) -> bytes:
    """Decode using module base64 for base85"""
    return b64.b85decode(data)

def is_valid(data: str) -> bool:
    """Check if string is base64 for base85"""
    try:
        bytes.fromhex(data)
        return True
    except:
        return False