# **Fast-Cryptography**
[![Apache License 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) [![PyPI version](https://img.shields.io/pypi/v/fast-cryptography.svg)](https://pypi.org/project/fast-cryptography/)




**Fast-Cryptography** - This is a library with cryptographic operations, including asymmetric and symmetric encryption, signatures, and hashes. `We use modern cryptographic technologies!`. **This module was created for lazy developers.**

> **Developer: `Alexx-coder or alexx (GitHub)`**

> **Version: `0.1.2`**

> **License: `Apache License 2.0`**

> **[Fast-Cryptography on Github](https://github.com/Alexx-coder/Fast-Cryptography.git)**

> **[Fast-Cryptography on PyPi](https://pypi.org/project/fast-cryptography/)**

> **Install:**

```bash
pip install fast-cryptography
```


## Acknowledgements

**This project uses:**
- **[cryptography](https://github.com/pyca/cryptography) `(Apache-2.0)`**
- **[pycryptodome](https://github.com/Legrandin/pycryptodome) `(BSD-2-Clause)`**
- **[base58](https://github.com/keis/base58) `(MIT)`**
- **[numpy](https://github.com/numpy/numpy) `(BSD-3-Clause)`**
- **[base45](https://github.com/kirei/python-base45) `(BSD-2-Clause)`**  

---

# **Modules and Technologies**

> **Learn about functions and how to work with them in another section**

## Asymmetric

- More detailed:

| Modules | Technologies (Python) |
|---------|-----------------------|
| RSA | `RSA, Serialization, Padding, Base64` |
| ECC | `ECC, secp256k1, Serialization, SHA256, Base64` |
| Ed25519 | `Ed25519, Serialization, Base64` |

- We are use modules on Python: `cryptography`, `base64`

## Symmetric

- More detailed:

| Modules | Technologies (Python) |
|---------|-----------------------|
| AES (128/256) | `Cipher`,`algorithms`, `modes` `PKCS7`, `Base64`, `Secrets`  |
| ChaCha20 | `Cipher` , `algorithms`, `modes` , `Base64`, `Secrets` |
| Fernet | `Fernet` |

- We are use modules on Python: `cryptography`, `base64`, `secrets`

## Hashes

- More detailed:

| Modules | Technologies (Python) |
|---------|-----------------------|
| SHA256 | `Hashlib` , `Secrets` |
| SHA512 | `Hashlib` , `Secrets` |
| SHA384 | `Hashlib` , `Secrets` |
| SHA224 | `Hashlib` , `Secrets` |
| SHA1 | `Hashlib` , `Secrets` |
| SHA3_256 | `Hashlib` , `Secrets` |
| SHA3_512 | `Hashlib` , `Secrets` |
| SHA3_384 | `Hashlib` , `Secrets` |
| SHA3_224 | `Hashlib` , `Secrets` |
| Blake2b | `Hashlib` , `Secrets` |
| Blake3s | `Hashlib` , `Secrets` |
| MD5 | `Hashlib` , `Secrets` |
| MD4 | `pycryptodome (Crypto.Hash MD4)`, `Secrets` |
| Ripemd160 | `pycryptodome (Crypto.Hash RIPEMD160)` , `Secrets` |

- We are use modules on Python: `hashlib`, `secrets`, `pycryptodome`

## Cryptorandom

- More detailed:

| Modules | Technologies (Python) |
|---------|-----------------------|
| Byte | `Secrets`, `os`, `uuid`, `random` |
| Hex_bytes | `Secrets` , `binascii` |
| Salt | `Secrets` |
| Nonce | `Secrets` |
| IV | `Secrets` |
| Choice | `Secrets`, `random`, `numpy` |
| Randint | `Secrets`, `random` |

- We are use modules on Python: `Secrets`, `os`, `random`, `uuid`, `binascii`, `numpy`

## Encoding

- More detailed:

| Modules | Technologies (Python) |
|---------|-----------------------|
| Base64 | `Base64` |
| Base58 | `Base58` |
| Base32 | `Base64: Base32` |
| Base16 | `Base64: Base16` |
| Base85 | `Base64: Base85` |
| BaseA85 | `Base64: Base85` |
| Base45 | `Base45` |

- We are use modules on Python: `Base64`, `Base58`, `Base45`

## Scripts

- More detailed:

| Modules | Technologies (Python) |
|---------|-----------------------|
| Password | `Cryptography`, `Secrets`, `Base64`, `PBKDF2HMAC`, `SHA256` |
| What_Encoding | `Base64 (Base64, Base32, Base16, Base85, BaseA85)`, `Base58`, `Base45` |

- We are use modules on Python: `cryptography`, `secrets`, `base64`, `base58`, `base45`



---


# **Working with functions**

## Asymmetric

> **There are 3 modules in total: RSA, ECC, Ed25519**

### RSA

- There are 3 functions in total: `rsa_gen_keys_pem()`, `rsa_encrypt()`, `rsa_decrypt()`

- How import:

```python
from fast_cryptography.algorithms.asymmetric.rsa import rsa_encrypt, rsa_decrypt, rsa_gen_keys_pem # Import functions
```

- Or:

```python
from fast_cryptography.algorithms.asymmetric import rsa # Import module
```

- How it works `gen_keys_pem()`:

| Stages |
|--------|
| Generation |
| Serialization |
| Print your keys: private and public |

- And in code:

```python
from fast_cryptography.algorithms.asymmetric.rsa import rsa_gen_keys_pem

keys = rsa_gen_keys_pem() # We do not specify attributes
print(keys) 
```


- Now how it works `rsa_encrypt()`;

| Stages | 
|--------|
| Load public key |
| Encrypting |
| Print: encrypted message in the format `Base64` |

- And in code:

```python
from fast_cryptography.algorithms.asymmetric.rsa import rsa_encrypt, rsa_gen_keys_pem

keys = rsa_gen_keys_pem()
public_pem = keys['public']

encryption = rsa_encrypt("Your message", public_pem) # Specify the message and your public key (preferably as a variable)
print(encryption)
```

- And at the end how it works `rsa_decrypt()`:

| Stages |
|--------|
| Load private key |
| Decrypting |
| Print: message |

- And in code:

```python
from fast_cryptography.algorithms.asymmetric.rsa import rsa_decrypt, rsa_gen_keys_pem, rsa_encrypt

keys = rsa_gen_keys_pem()
private_pem = keys['private']
public_pem = keys['public']

encryption = rsa_encrypt("Your message", public_pem)

decryption = rsa_decrypt(encryption, private_pem) # Specify the encrypted message and your private key (preferably as a variable)
print(decryption)
```

### ECC

- There are 3 functions in total: `ecc_gen_keys_pem()`, `ecc_sign()`, `ecc_verify()`

- How import:

```python
from fast_cryptography.algorithms.asymmetric.ecc import ecc_gen_keys_pem, ecc_sign, ecc_verify
```

- Or:

```python
from fast_cryptography.algorithms.asymmetric import ecc
```


- How it works `ecc_gen_keys_pem()`:

| Stages |
|--------|
| Generation |
| Serialization |
| Print your keys: private and public |

- And in code:

```python
from fast_cryptography.algorithms.asymmetric.ecc import ecc_gen_keys_pem

keys = ecc_gen_keys_pem() # We do not specify attributes
print(keys)
```

- Now how it works `ecc_sign`:

| Stages |
|--------|
| Load private key |
| Signing up |
| Print: signature in formate `Base64` |

- And in code:

```python
from fast_cryptography.algorithms.asymmetric.ecc import ecc_gen_keys_pem, ecc_sign
keys = ecc_gen_keys_pem() 
private_pem = keys['private']

signature = ecc_sign("Your message", private_pem) # Specify the message and your private key (preferably as a variable)
print(signature)
```

- And at the end how it works `ecc_verify()`:

| Stages |
|--------|
| Load public key |
| Verifying signature |
| Print: True or False |

- And in code:

```python
from fast_cryptography.algorithms.asymmetric.ecc import ecc_gen_keys_pem, ecc_sign, ecc_verify

keys = ecc_gen_keys_pem()
private_pem = keys['private']
public_pem = keys['public']

siganture = ecc_sign("Your message", private_pem)

verify = ecc_verify("Your message", signature, public_pem)
print(verify)
```

### Ed25519

- There are 3 functions in total: `ed25519_gen_keys_pem()`, `ed25519_sign()`, `ed25519_verify()`

- How import:

```python
from fast_cryptography.algorithms.asymmetric.ed25519 import ed25519_gen_keys_pem, ed25519_sign, ed25519_verify
```

- Or:

```python
from fast_cryptography.algorithms.asymmetric import ed25519
```

- How it works `ed25519_gen_keys_pem()`

| Stages | 
|--------| 
| Generation | 
| Serialization | 
| Print your keys: private and public | 

- And in code:

```python
from fast_cryptography.algorithms.asymmetric.ed25519 import ed25519_gen_keys_pem

keys = ed25519_gen_keys_pem() # We do not specify attributes
print(keys)
```

- Now how it works `ed25519_sign()`:

| Stages |
|--------|
| Load private key |
| Signing up |
| Print: signature in format `Base64` |

- And in code:

```python
from fast_cryptography.algorithms.asymmetric.ed25519 import ed25519_gen_keys_pem, ed25519_sign

keys = ed25519_gen_keys_pem()
private_pem = keys['private']

signature = sign("Your message", private_pem) # Specify the message and your private key (preferably as a variable)
```

- And at the end how it works `ed25519_verify()`:

| Stages |
|--------|
| Load public key |
| Verifying signature |
| Print: True or False |

- And in code:

```python
from fast_cryptography.algorithms.asymmetric.ed25519 import ed25519_gen_keys_pem, ed25519_sign, ed25519_verify

keys = ed25519_gen_keys_pem()
private_pem = keys['private']
public_pem = keys['public']

signature = ed25519_sign("Your message", private_pem)

verify = ed25519_verify("Your message", signature, public_pem)
print(verify)
```

## Symmetric

> **There are 3 modules in total: Fernet, AES, ChaCha20**

### Fernet

- There are 3 functions in total: `fernet_generate_key()`, `fernet_encrypt()`, `fernet_decrypt()`

- How import:

```python
from fast_cryptography.algorithms.symmetric.fernet import fernet_generate_key, fernet_encrypt, fernet_decrypt
```

- Or:

```python
from fast_cryptography.algorithms.symmetric import fernet
```

- How it works `fernet_generate_key()`

| Stages | 
|--------| 
| Generation | 
| Decode in UTF-8 | 
| Print your key| 

- And in code:

```python
from fast_cryptography.algorithms.symmetric.fernet import fernet_generate_key

key = fernet_generate_key() # We do not specify attributes
print(key)
```

- Now how it works `fernet_encrypt()`:

| Stages |
|--------|
| Encode your key for cipher |
| Encrypting |
| Print: your encrypted message in UTF-8 |

- And in code:

```python
from fast_cryptography.algorithms.symmetric.fernet fernet_generate_key, fernet_encrypt

key = fernet_generate_key()

encrypt = fernet_encrypt("Your message", key) # Specify the message and your key (preferably as a variable)
print(encrypt)
```

- And at the end how it works `fernet_decrypt()`:

| Stages |
|--------|
| Encode your key for cipher|
| Decrypting |
| Print: your decrypted message |

- And in code:

```python
from fast_cryptography.algorithms.symmetric.fernet import fernet_generate_key, fernet_encrypt, fernet_decrypt

key = fernet_generate_key()

encrypt = fernet_encrypt("Your message", key)

decrypted = fernet_decrypt(encrypt, key) # Specify the encrypted message and your key (preferably as a variable)
```


### AES

- There are 3 functions in total: `aes_generate_key()`, `aes_encrypt()`, `aes_decrypt()`

- How import:

```python
from fast_cryptography.algorithms.symmetric.aes import aes_generate_key, fernet_encrypt, fernet_decrypt
```

- Or:

```python
from fast_cryptography.algorithms.symmetric import aes
```

- How it works `aes_generate_key()`

| Stages | 
|--------| 
| Generation | 
| Decode in base64 | 
| Print your key | 

- And in code:

```python
from fast_cryptography.algorithms.symmetric.aes import aes_generate_key

size = # 16 (AES-128), 24 (AES-192) or 32 (AES-256)

key = aes_generate_key(size) # We do specify attribute key size (16, 24 or 32)
print(key)
```

- Now how it works `aes_encrypt()`:


| Stages |
|--------|
| Encode message to bytes |
| Decode key from Base64 |
| Generate random IV (16 bytes) |
| Create AES cipher in CBC mode with IV |
| Create PKCS7 padder (block size 16) |
| Pad the message |
| Encrypt padded message |
| Combine IV + ciphertext |
| Encode result to Base64 |


- And in code:

```python
from fast_cryptography.algorithms.symmetric.aes import aes_generate_key, aes_encrypt

size = # 16 (AES-128), 24 (AES-192) or 32 (AES-256)

key = aes_generate_key(size)

encrypt = aes_encrypt("Your message", key) # Specify the message and your key (preferably as a variable)
print(encrypt)
```

- And at the end how it works `aes_decrypt()`:

| Stages |
|--------|
| Decode encrypted data from Base64 |
| Decode key from Base64 |
| Extract IV (first 16 bytes) |
| Extract ciphertext (remaining bytes) |
| Create AES cipher in CBC mode with IV |
| Decrypt ciphertext |
| Unpad decrypted data (PKCS7) |
| Decode bytes to string |

- And in code:

```python
from fast_cryptography.algorithms.symmetric.aes import aes_generate_key, aes_encrypt, aes_decrypt

size = # 16 (AES-128), 24 (AES-192) or 32 (AES-256)

key = aes_generate_key(size)

encrypt = aes_encrypt("Your message", key) 

decrypted = aes_decrypt(encrypted, key)  # Specify the encrypted message and your key (preferably as a variable)
```

### ChaCha20

- There are 3 functions in total: `chacha20_generate_key()`, `chacha20_encrypt()`, `chacha20_decrypt()`


- How import:

```python
from fast_cryptography.algorithms.symmetric.chacha20 import chacha20_generate_key, chacha20_encrypt, chacha20_decrypt
```

- Or:

```python
from fast_cryptography.algorithms.symmetric import chacha20
```

- How it works `chacha20_generate_key()`:

| Stages |
|--------|
| Generation | 
| Decode in base64 | 
| Print your key | 

- And in code

```python
from fast_cryptography.algorithms.symmetric.chacha20 import chacha20_generate_key

key = chacha20_generate_key() 
print(key)
```


- Now how it works `chacha20_encrypt()`:

| Stages |
|--------|
| Encode message to bytes |
| Decode key from Base64 |
| Generate random nonce (16 bytes) |
| Create ChaCha20 cipher with nonce |
| Encrypt message |
| Combine nonce + ciphertext |
| Encode result to Base64 |


- And in code:

```python
from fast_cryptography.algorithms.symmetric.chacha20 import chacha20_generate_key, chacha20_encrypt

key = chacha20_generate_key()

encrypt = chacha20_encrypt("Your message", key) # Specify the message and your key (preferably as a variable)
print(encrypt)
```

- And at the end how it works `chacha20_decrypt()`:

| Stages |
|--------|
| Decode encrypted data from Base64 |
| Decode key from Base64 |
| Extract nonce (first 16 bytes) |
| Extract ciphertext (remaining bytes) |
| Create ChaCha20 cipher with nonce |
| Decrypt ciphertext |
| Decode bytes to string |


- And in code:

```python
from fast_cryptography.algorithms.symmetric.chacha20 import chacha20_generate_key, chacha20_encrypt, chacha20_decrypt

key = chacha20_generate_key()

encrypt = chacha20_encrypt("Your message", key) 

decrypted = chacha20_decrypt(encrypted, key)  # Specify the encrypted message and your key (preferably as a variable)
```

## Hashes

> **We are use the best hashes and the worst hashes in this libraly**

> **Warning: For security use size salt: 32 Bytes. But can use 16-64 Bytes. GoodLuck!**

- `All hashes have the same stages.`


- How they works:

| Stages |
|--------|
| Generation salt (bytes) |
| Generation hash: `your message + salt + encode` |
| Print: hash |

- And in code (all) :

```python
from fast_cryptography.algorithms.hashes.md4 import hash_md4
from fast_cryptography.algorithms.hashes.md5 import hash_md5
from fast_cryptography.algorithms.hashes.ripemd160 import hash_ripemd160
from fast_cryptography.algorithms.hashes.sha1 import hash_sha1
from fast_cryptography.algorithms.hashes.sha224 import hash_sha224
from fast_cryptography.algorithms.hashes.sha256 import hash_sha256
from fast_cryptography.algorithms.hashes.sha384 import hash_sha384
from fast_cryptography.algorithms.hashes.sha512 import hash_sha512
from fast_cryptography.algorithms.hashes.sha3_224 import hash_sha3_224
from fast_cryptography.algorithms.hashes.sha3_256 import hash_sha3_256
from fast_cryptography.algorithms.hashes.sha3_384 import hash_sha3_384
from fast_cryptography.algorithms.hashes.sha3_512 import hash_sha3_512
from fast_cryptography.algorithms.hashes.blake2b import hash_blake2b
from fast_cryptography.algorithms.hashes.blake2s import hash_blake2s

message = 'Your message'
size = 32

# Список хэш-функций
hashes = [
    hash_md4, hash_md5, hash_ripemd160,
    hash_sha1, hash_sha224, hash_sha256,
    hash_sha384, hash_sha512,
    hash_sha3_224, hash_sha3_256, hash_sha3_384, hash_sha3_512,
    hash_blake2b, hash_blake2s
]

print("=== Testing hashes ===\n")
for h in hashes:
    hash_val, salt = h(message, size)
    print(f"{h.__name__} | {hash_val}... | Salt: {salt}...")
```

## Cryptorandom

> **Here 7 modules: `byte`, `hex_bytes`, `salt`, `nonce`, `iv`, `choice`, `randint`**


### Byte

- How import:

```python
from fast_cryptography.algorithms.cryptorandom.byte import  bytes_token, bytes_urandom, bytes_uuid, bytes_random
```

- Or:

```python
from fast_cryptography.algorithms.cryptorandom import byte
```

- How they works:

| Stages |
|--------|
| Generation bytes use definite algorithm |
| Print: bytes |

- Algorithms:

| Algorithms on Python |
|----------------------|
| Secrets (Module name): `bytes_token` |
| OS (Module name): `bytes_urandom` |
| UUID 4 (Module name - uuid): `bytes_uuid` |
| Random (Module name: `bytes_random`) |

- And in code:

```python
from fast_cryptography.algorithms.cryptorandom.byte import
bytes_token, bytes_urandom, bytes_uuid, bytes_random

print(bytes_token(32)) # I'm use 32 bytes. But can you use 16-64 bytes. 32 bytes it's safe
print(bytes_urandom(32))
print(bytes_uuid(32))
print(bytes_random(32))

# WARNINGS!!! Don't forget to specify the quantity of bytes.
```

### Hex_bytes

- How import:

```python
from fast_cryptography.algorithms.cryptorandom.hex_bytes import hex_token, hex_token_bytes, encode_hex, decode_hex, hex2text, text2hex, is_valid_hex
```

- Or:

```python
from fast_cryptography.algorithms.cryptorandom import hex_bytes
```

- In code:

```python
ffrom fast_cryptography.algorithms.cryptorandom.hex_bytes import hex_token, hex_token_bytes, encode_hex, decode_hex, hex2text, text2hex, is_valid_hex

print(hex_token(16)) # Don't forget to specify the quantity of bytes.
print(hex_token_bytes(16))

data = b"Hello, bro!"
hex_str = encode_hex(data)
print(hex_str)

decoded = decode_hex(hex_str)
print(decoded)

print(hex2text("48656c6c6f"))

print(text2hex("Hello"))

print(is_valid_hex("48656c6c6f"))
print(is_valid_hex("GGG"))
```

### Salt

> **Size salt in bytes: 16-64**

- How import:

```python
from fast_cryptography.algorithms.cryptorandom.salt import salt_gen, salt_gen_hex
```

- Or:

```python
from fast_cryptography.algorithms.cryptorandom import salt
```

- How it works `salt_gen()`:

| Stages |
|--------|
| Generation bytes |
| Print: salt |

- And how it works `salt_gen_hex()`:

| Stages |
|--------|
| Generation bytes |
| Print: salt in format hex |

- In code:

```python
from fast_cryptography.algorithms.cryptorandom.salt import salt_gen, salt_gen_hex

print(salt_gen(32)) # Don't forget to specify the quantity of bytes.
print(salt_gen_hex(32))
```

### Nonce

> **Size nonce in bytes: 12-16**

- How import:

```python
from fast_cryptography.algorithms.cryptorandom.nonce import nonce_gen, nonce_gen_hex
```

- Or:

```python
from fast_cryptography.algorithms.cryptorandom import nonce
```

- How it works `nonce_gen()`:

| Stages |
|--------|
| Generation bytes |
| Print: nonce |

- And how it works `nonce_gen_hex()`:

| Stages |
|--------|
| Generation bytes |
| Print: nonce in format hex |


- In code:

```python
from fast_cryptography.algorithms.cryptorandom.nonce import nonce_gen, nonce_gen_hex

print(nonce_gen()) # You can choose not to specify a size nonce (only 16), or you can specify (12-16)
print(nonce_gen_hex())
```

### IV

> **Size iv in bytes: only 16**

- How import:

```python
from fast_cryptography.algorithms.cryptorandom.iv import iv_gen, iv_gen_hex
```

- Or:

```python
from fast_cryptography.algorithms.cryptorandom import iv
```

- How it works `iv_gen()`:

| Stages |
|--------|
| Generation bytes |
| Print: iv |

- And how it works `iv_gen_hex()`:

| Stages |
|--------|
| Generation bytes |
| Print: iv in format hex |


- In code:

```python
from fast_cryptography.algorithms.cryptorandom.nonce import iv_gen, iv_gen_hex

print(iv_gen()) # You don't need to specify the size iv, size iv only 16 bytes
print(iv_gen_hex())
```

### Choice

- How import:

```python
from fast_cryptography.algorithms.cryptorandom.choice import crypto_choice, random_choice, random_choices, scientific_choice
```

- Or:

```python
from fast_cryptography.algorithms.cryptorandom import choice
```


- How it works:

| Stages |
|--------|
| Selects using its own algorithm |
| Print: what did he choose |

- In code:

```python
from fast_cryptography.algorithms.cryptorandom.choice import crypto_choice, random_choice, random_choices, scientific_choice

choice = ['1', '2'] # I'm showing you on the example, but you create mine

# Warning: don't forget to specify the variable (choice for example)

print(crypto_choice(choice))
print(random_choice(choice))
print(random_choices(choice))
print(scientific_choice(choice))
```


### Randint

- How import:

```python
from fast_cryptography.algorithms.cryptorandom.randint import crypto_randbelow, crypto_randint, random_randint
```

- Or:

```python
from fast_cryptography,algorithms.cryptorandom import randint
```

- How it works `crypto_randbelow`:

| Stages |
|--------|
| Selects a random (use cryptography) number from number 0 up to a number (selected by you) |
| Print: selected number |

- And how it works `crypto_randint` and `random_randint`:

| Stages |
| Selects a random (use cryptography or not) number (selected by you) up to a number (selected by you) |
| Print: selected number |

- And in code:

```python
from fast_cryptography.algorithms.cryptorandom.randint import crypto_randbelow, crypto_randint, random_randint

number_one = 21 # For example (variable for all function)
number_two = 1221 # For example (variable for crypto_randint and random_randint)

# Warning: don't forget to specify the variable

print(crypto_randbelow(number_one)) #
print(crypto_randint(number_one, number_two))
print(random_randint(number_one, number_two))
```

## Encoding

> **Here 7 modules: `base64`, `base58`, `base45`, `base32`, `base16`, `base85`, `baseA85`**

### Base64

- How import:

```python
from fast_cryptography.algorithms.encoding.base64 import base64_encode, base64_decode, base64_url_encode, base64_url_decode, is_valid_base64
```

- Or:

```python
from fast_cryptography.algorithms.encoding import base64
```


- How it works: `base64_encode` and `base64_decode`:

| Stages |
|--------|
| Encoding your message or decoding your message in formate base64 |
| Print: encoded message in formate base64 or decoded message |

- How it works `base64_url_encode` and `base64_url_decode`:

| Stages |
|--------|
| Encoding your message for url or decoding your message in formate base64 for url |
| Print: encoded message in formate base64 for url or decoded message |

- And how it works `is_valid_base64`:

| Stages |
|--------|
| Checks if the text is valid in formate base64 |
| Print: return True or False |

- And in code:

```python
from fast_cryptography.algorithms.encoding.base64 import base64_encode, base64_decode, base64_url_encode, base64_url_decode, is_valid_base64

text = b'Python' # For example

# Base64
encoded = base64_encode(text)
print(encoded)
decoded = base64_decode(encoded)
print(encode)

# Base64 for url

encoded_url = base64_url_encode(text)
print(encoded_url)
decoded_url = base64_url_decode(encoded_url)
print(decoded)

# Is valid 

print(is_valid_base64(encoded)) # True or False
# Or
return is_valid_base64(encoded)
```

### Base58

- How import:

```python
from fast_cryptography.algorithms.encoding.base58 import base58_encode, base58_decode, is_valid_base58
```

- Or:

```python
from fast_cryptography.algorithms.encoding import base58
```

- How it works `base58_encode`:

| Stages |
|--------|
| Encoding your message in formate Base58 |
| Print: encoded your message in formate Base58 |

- How it works `base58_decode`:

| Stages |
|--------|
| Decoding message (in formate base58) in text |
| Print: decoded message |

- And how it works `is_valid_base58`:

| Stages |
|--------|
| Checks if the text is valid in formate base58 |
| Print: return True or False |

- And in code:

```python
from fast_cryptography.algorithms.encoding.base64 import base58_encode, base58_decode, is_valid_base58

text = b'Python'

# Base58
encoded = base58_encode(text)
print(encoded)
decoded = base58_decode(encoded)
print(decoded)

# Is valid
print(is_valid_base58(encoded)) # True or False
# Or
return is_valid_base58(encodedd)
```

### Base45

- How import:

```python
from fast_cryptography.algorithms.encoding.base45 import base45_encode, base45_decode, is_valid_base45
```

- Or:

```python
from fast_cryptography.algorithms.encoding import base45
```

- How it works `base45_encode`:

| Stages |
|--------|
| Encoding your message in formate Base45 |
| Print: encoded your message in formate Base45 |

- How it works `base45_decode`:

| Stages |
|--------|
| Decoding message (in formate base45) in text |
| Print: decoded message |

- And how it works `is_valid_base45`:

| Stages |
|--------|
| Checks if the text is valid in formate base45 |
| Print: return True or False |

- And in code:

```python
from fast_cryptography.algorithms.encoding.base45 import base45_encode, base45_decode, is_valid_base45

text = b'Python'

# Base58
encoded = base45_encode(text)
print(encoded)
decoded = base45_decode(encoded)
print(decoded)

# Is valid
print(is_valid_base45(encoded)) # True or False
# Or
return is_valid_base45(encodedd)
```

### Base32

- How import:

```python
from fast_cryptography.algorithms.encoding.base32 import base32_encode, base32_decode, is_valid_base32
```

- Or:

```python
from fast_cryptography.algorithms.encoding import base32
```

- How it works `base32_encode`:

| Stages |
|--------|
| Encoding your message in formate Base32 |
| Print: encoded your message in formate Base32 |

- How it works `base32_decode`:

| Stages |
|--------|
| Decoding message (in formate base32) in text |
| Print: decoded message |

- And how it works `is_valid_base32`:

| Stages |
|--------|
| Checks if the text is valid in formate base32 |
| Print: return True or False |

- And in code:

```python
from fast_cryptography.algorithms.encoding.base32 import base32_encode, base32_decode, is_valid_base32

text = b'Python'

# Base58
encoded = base32_encode(text)
print(encoded)
decoded = base32_decode(encoded)
print(decoded)

# Is valid
print(is_valid_base32(encoded)) # True or False
# Or
return is_valid_base32(encodedd)
```

### Base16

- How import:

```python
from fast_cryptography.algorithms.encoding.base16 import base16_encode, base16_decode, is_valid_base16
```

- Or:

```python
from fast_cryptography.algorithms.encoding import base16
```

- How it works `base16_encode`:

| Stages |
|--------|
| Encoding your message in formate Base16 |
| Print: encoded your message in formate Base16 |

- How it works `base16_decode`:

| Stages |
|--------|
| Decoding message (in formate base16) in text |
| Print: decoded message |

- And how it works `is_valid_base16`:

| Stages |
|--------|
| Checks if the text is valid in formate base16 |
| Print: return True or False |

- And in code:

```python
from fast_cryptography.algorithms.encoding.base45 import base16_encode, base16_decode, is_valid_base16

text = b'Python'

# Base58
encoded = base16_encode(text)
print(encoded)
decoded = base16_decode(encoded)
print(decoded)

# Is valid
print(is_valid_base16(encoded)) # True or False
# Or
return is_valid_base16(encodedd)
```


### Base85

- How import:

```python
from fast_cryptography.algorithms.encoding.base85 import base85_encode, base85_decode, is_valid_base85
```

- Or:

```python
from fast_cryptography.algorithms.encoding import base85
```

- How it works `base85_encode`:

| Stages |
|--------|
| Encoding your message in formate Base85 |
| Print: encoded your message in formate Base85 |

- How it works `base85_decode`:

| Stages |
|--------|
| Decoding message (in formate base85) in text |
| Print: decoded message |

- And how it works `is_valid_base85`:

| Stages |
|--------|
| Checks if the text is valid in formate base85 |
| Print: return True or False |

- And in code:

```python
from fast_cryptography.algorithms.encoding.base85 import base85_encode, base85_decode, is_valid_base85

text = b'Python'

# Base58
encoded = base85_encode(text)
print(encoded)
decoded = base85_decode(encoded)
print(decoded)

# Is valid
print(is_valid_base85(encoded)) # True or False
# Or
return is_valid_base85(encodedd)
```

### BaseA85

- How import:

```python
from fast_cryptography.algorithms.encoding.baseA85 import baseA85_encode, baseA85_decode, is_valid_baseA85
```

- Or:

```python
from fast_cryptography.algorithms.encoding import baseA85
```

- How it works `baseA85_encode`:

| Stages |
|--------|
| Encoding your message in formate BaseA85 |
| Print: encoded your message in formate BaseA85 |

- How it works `baseA85_decode`:

| Stages |
|--------|
| Decoding message (in formate baseA85) in text |
| Print: decoded message |

- And how it works `is_valid_baseA85`:

| Stages |
|--------|
| Checks if the text is valid in formate baseA85 |
| Print: return True or False |

- And in code:

```python
from fast_cryptography.algorithms.encoding.baseA85 import baseA85_encode, baseA85_decode, is_valid_baseA85

text = b'Python'

# Base58
encoded = baseA85_encode(text)
print(encoded)
decoded = baseA85_decode(encoded)
print(decoded)

# Is valid
print(is_valid_baseA85(encoded)) # True or False
# Or
return is_valid_baseA85(encodedd)
```

## Scripts

> **Here 2 modules: `password`, `what_encoding`**


### Password

- How import:

```python
from fast_cryptography.algorithms.scripts.password import auth, verify
```

- Or:

```python
from fast_cryptography.algorithms.scripts import password
```

- How it works `auth`:

| Stages |
|--------|
| Takes password |
| Generating salt (32 bytes default) |
| Transmits password and salt in PBKDF2HMAC |
| Does 100.000 iteration SHA-256 |
| Receives hash |
| Encoding hash in Base64 |
| Encoding salt in HEX |
| Return in tuple: hash (Base64) and salt (HEX) |

- In code:

```python
from fast_cryptography.algorithms.scripts.password import auth

pwd = 'password' # For example, it's password don't safe!

return auth(pwd)
```

- And how it works `verify`:

| Stages |
|--------|
| Takes entered password |
| Takes salt (HEX in bytes) |
| Takes hash (Base64 in bytes) |
| Recalculates hash through PBKDF2 use the same salt |
| Check with safe hash |
| Print: return True or False |

- In code:

```python 
from fast_cryptography.algorithms.scripts.password import auth, verify

# Auth
pwd = 'password'
hash_val, salt = auth(pwd)

# Verify
your_pwd = input("Enter password: ").strip()
if verify(your_pwd, hash_val, salt):
    return "Correctly password", True
else:
    return "Uncorrectly password", False

```

## What_Encoding

- How import:

```python
from fast_cryptography.algorithms.scripts.what_encoding import what_encoding
```

- Or:

```python
from fast_cryptography.algorithms.scripts import what_encoding
```

- How it works:

| Stages |
|--------|
| Checks what the encoding is |
| Print: return encoding (For example: "Base64")

- And in code:

```python
from fast_cryptography.scripts.what_encoding import what_encoding

print(what_encoding("SGVsbG8="))      # Base64
print(what_encoding("9Ajdvzr"))       # Base58
print(what_encoding("48656c6c6f"))    # Base16 (HEX)
print(what_encoding("Hello"))         # Unknown
```

---
