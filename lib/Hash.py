import hashlib 
from pydantic import BaseModel

class Hashing_Model(BaseModel):
    author: str
    algorithm: str
    message: str
    result: str
        
    class Config:
        schema_extra  = {
            "example": {
                "author": "sndyarzxch",
                "algorithm": "SHA-512",
                "message": "Hello Elifia!",
                "result": "33c68c39965807ac94637aef182449e3a43c033a1f948637cff3a3330dcf53fd9325262cc4b6313cfb9c68286324c71646a67f915cbc1c98c0e9e7531dd3cbd9",
            }
        }

def Hashing(algo, text):
    if algo.lower() == "sha1" or algo.lower() == "sha-1":
        res = hashlib.sha1(text.encode("utf-8")).hexdigest()
    elif algo.lower() == "sha224" or algo.lower() == "sha-224":
        res = hashlib.sha224(text.encode("utf-8")).hexdigest()
    elif algo.lower() == "sha256" or algo.lower() == "sha-256":
        res = hashlib.sha256(text.encode("utf-8")).hexdigest()
    elif algo.lower() == "sha512" or algo.lower() == "sha-512":
        res = hashlib.sha512(text.encode("utf-8")).hexdigest()
    elif algo.lower() == "md5" or algo.lower() == "md-5":
        res = hashlib.md5(text.encode("utf-8")).hexdigest()
    else:
        res = "Invalid algo baka! There only available SHA1, SHA224, SHA256, SHA512, and MD5 -_-"
    return res