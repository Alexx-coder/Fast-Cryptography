from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
import base64


def gen_keys_pem() -> dict:
    """Generates an Ed25519 key pair in PEM format"""
    private_key = ed25519.Ed25519PrivateKey.generate()
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
        'private':private_pem,
        'public':public_pem
    }




def sign(message: str, private_key_pem: str) -> str:
    """Signs a message using Ed25519 private key"""
    private_key = serialization.load_pem_private_key(
        private_key_pem.encode(),
        password=None
    )

    signature = private_key.sign(
        message.encode('utf-8')
    )
    return base64.b64encode(signature).decode('utf-8')

def verify(message: str, signature_b64: str, public_key_pem: str) -> bool:
    """Verifies an Ed25519 signature using public key"""
    public_key = serialization.load_pem_public_key(public_key_pem)
    signature = base64.b64decode(signature_b64)

    try:
        public_key.verify(
            signature,
            message.encode('utf-8')
        )

        return True
    
    except:
        return False
    
    