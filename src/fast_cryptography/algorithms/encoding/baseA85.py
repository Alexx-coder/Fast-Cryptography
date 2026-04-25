import base64 as b64

def encode(data: bytes) -> str:
    """Encode using module base64 for baseA85"""
    return b64.a85encode(data).decode()

def decode(data: str) -> bytes:
    """Decode using module base64 from baseA85"""
    return b64.a85decode(data)

def is_valid(data: str) -> bool:
    """Check if string is base64 for baseA85"""
    try:
        bytes.fromhex(data)
        return True
    except:
        return False   