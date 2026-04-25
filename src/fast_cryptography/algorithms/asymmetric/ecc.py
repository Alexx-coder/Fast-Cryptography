from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
import base64


def gen_keys_pem() -> dict:
    """Generates an ECC key pair (secp256k1) in PEM format"""
    private_key = ec.generate_private_key(ec.SECP256K1())
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


def sign(message: str, private_key_pem: str) -> str:
    """Signs a message using ECC private key"""
    private_key = serialization.load_pem_private_key(
        private_key_pem.encode(),
        password=None
    )
    
    signature = private_key.sign(
        message.encode(),
        ec.ECDSA(hashes.SHA256())
    )
    return base64.b64encode(signature).decode('utf-8')


def verify(message: str, signature_b64: str, public_key_pem: str) -> bool:
    """Verifies an ECC signature using public key"""
    public_key = serialization.load_pem_public_key(public_key_pem.encode())
    signature = base64.b64decode(signature_b64)
    
    try:
        public_key.verify(
            signature,
            message.encode('utf-8'),
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except:
        return False