import secrets

def iv_gen(byte: 16) -> bytes:
    """Generator iv using module secrets
    Bytes 16"""
    return secrets.token_bytes(byte)

def iv_gen_hex(byte: 16) -> str:
    """Generator iv bytes to hex using module secrets
    Bytes 16"""
    return iv_gen().hex()

