import secrets
import binascii

def hex_token(byte: int) -> str:
    """Generate hex string using secrets (safe)"""
    return secrets.token_hex(byte)

def hex_token_bytes(byte: int) -> str:
    """Generate hex string via bytes using secrets (safe)"""
    return secrets.token_bytes(byte).hex()

def encode_hex(data: bytes) -> str:
    """Encode bytes to hex string"""
    return binascii.hexlify(data).decode('utf-8')

def decode_hex(hex_str: str) -> bytes:  
    """Decode hex string to bytes"""
    return binascii.unhexlify(hex_str)

def hex2text(hex_str: str) -> str:
    """Convert hex string to text (UTF-8)"""
    return decode_hex(hex_str).decode('utf-8', errors='replace')

def text2hex(text: str) -> str:
    """Convert text to hex string"""
    return encode_hex(text.encode('utf-8'))

def is_valid_hex(hex_str: str) -> bool:
    """Check if string is valid hex"""
    try:
        bytes.fromhex(hex_str)
        return True
    except (binascii.Error, ValueError):
        return False