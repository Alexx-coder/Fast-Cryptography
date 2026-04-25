def what_encoding(data: str) -> str:
    """Defines the encoding of the string"""

    try:
        import base64
        base64.b64decode(data)
        return "Base64"
    except:
        pass


    try:
        import base45
        base45.b45decode(data)
        return "Base45"
    except:
        pass
    
    try:
        import base58
        base58.b58decode(data)
        return "Base58"
    except:
        pass
    
    try:
        import base64
        base64.urlsafe_b64decode(data)
        return "Base64 URL"
    except:
        pass
    
    try:
        import base64
        base64.b64decode(data)
        return "Base64"
    except:
        pass
    
    try:
        import base64
        base64.b32decode(data)
        return "Base32"
    except:
        pass
    
    try:
        import base64
        base64.b85decode(data)
        return "Base85"
    except:
        pass

    try:
        import base64
        base64.a85decode(data)
        return "BaseA85"
    except:
        pass
    
    try:
        bytes.fromhex(data)
        return "Base16 (HEX)"
    except:
        pass
    
    return "Unknown"
