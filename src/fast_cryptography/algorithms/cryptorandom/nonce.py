import secrets

def nonce_gen(byte: int = 16) -> bytes:
    """Generate nonce bytes (12-16 bytes recommended)"""
    return secrets.token_bytes(byte)

def nonce_gen_hex(byte: int = 16) -> str:
    """Generate nonce as hex string"""
    return secrets.token_hex(byte)