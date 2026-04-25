import base45


def encode(data: bytes) -> str:
    """Encode bytes to Base45 string"""
    return base45.b45encode(data).decode()


def decode(s: str) -> bytes:
    """Decode Base45 string to bytes"""
    return base45.b45decode(s)


def is_valid(s: str) -> bool:
    """Check if string is valid Base45"""
    try:
        bytes.fromhex(s)
        return True
    except Exception:
        return False