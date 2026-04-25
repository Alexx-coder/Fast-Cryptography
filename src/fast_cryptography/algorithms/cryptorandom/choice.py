import secrets
import random
import numpy as np

def crypto_choice(choicen) -> str:
    """Cryptographically secure random choice"""
    return secrets.choice(choicen)

def random_choice(choicen) -> str:
    """Not secure random choice"""
    return random.choice(choicen)

def random_choices(choicen) -> str:
    """Not secure random choices"""
    return random.choices(choicen)

def scientific_choice(choicen) -> str:
    """Scientific random choice"""
    return np.random.choice(choicen)


