from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import base64

def gen_keys_pem(key_size=2048) -> dict:
    """Generates an RSA key pair in PEM format"""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size
    )
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ).decode('utf-8')

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')

    return {
        'private': private_pem,
        'public': public_pem
    }

def encrypt(message: str, public_pem: str) -> str:
    """Encrypts a message using an RSA public key"""
    public_key = serialization.load_pem_public_key(public_pem.encode())

    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return base64.b64encode(encrypted).decode()

def decrypt(encrypted_b64: str, private_key_pem: str) -> str:
    """Decrypts a message using an RSA private key"""
    private_key = serialization.load_pem_private_key(
        private_key_pem.encode(),
        password=None
    )
    
    encrypted = base64.b64decode(encrypted_b64)
    decrypted = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode()