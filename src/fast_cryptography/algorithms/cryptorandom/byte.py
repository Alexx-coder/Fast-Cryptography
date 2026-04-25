import secrets
import os
import random
import uuid

def bytes_token(byte: int) -> bytes:
    """Generate bytes using secrets (safe)"""
    return secrets.token_bytes(byte)

def bytes_urandom(byte: int) -> bytes:
    """Generate bytes using os.urandom (safe)"""
    return os.urandom(byte)

def bytes_uuid() -> bytes:
    """Generate 16 bytes using uuid (medium security)"""
    return uuid.uuid4().bytes

def bytes_random(byte: int) -> bytes:
    """Generate bytes using random (NOT SAFE for crypto!)"""
    return random.randbytes(byte)