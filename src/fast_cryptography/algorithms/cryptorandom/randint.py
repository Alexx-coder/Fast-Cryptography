import random
import secrets

def crypto_randbelow(number: int) -> int:
    """Return random integer in range (0, n)"""
    return secrets.randbelow(number)

def crypto_randint(a: int, b: int) -> int:
    """Return random integer in range [a, b] inclusive"""
    return secrets.randbelow(b - a + 1) + a

def random_randint(a: int, b: int) -> int:
    """Return random integer in range (0 , n)
    It's not safe"""
    return random.randint(a, b)
    



