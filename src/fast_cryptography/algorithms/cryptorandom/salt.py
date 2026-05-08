import secrets

def salt_gen(byte: int) -> bytes:
    """Generator salt using module secrets
    Bytes 16-64"""
    return secrets.token_bytes(byte)

def salt_gen_hex(byte: int) -> str:
    """Generator salt bytes to hex using module secrets
    Bytes 16-64"""
    return salt_gen(byte).hex()