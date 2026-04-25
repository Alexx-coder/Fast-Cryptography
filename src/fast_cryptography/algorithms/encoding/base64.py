import base64 as b64

def encode(data: bytes) -> str:
    """Encode using module base64"""
    return b64.b64encode(data).decode()

def decode(data: str) -> bytes:
    """Decode using module base64"""
    return b64.b64decode(data)

def url_encode(data: bytes) -> str:
    """Encode url using module base64"""
    return b64.urlsafe_b64encode(data).decode()

def url_decode(data: str) -> bytes:
    """Decode url using module base64"""
    return b64.urlsafe_b64decode(data)

def is_valid(data: str) -> bool:
    """Check if string is base64"""
    try:
        bytes.fromhex(data)
        return True
    except:
        return False
    