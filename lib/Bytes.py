import base64 as byte
from pydantic import BaseModel

class Encode_Model(BaseModel):
    author: str
    type: str
    message: str
    result: str
        
    class Config:
        schema_extra  = {
            "example": {
                "author": "sndyarzxch",
                "type": "base64",
                "message": "Hello Elifia!",
                "result": "SGVsbG8gRWxpZmlhIQ==",
            }
        }
        
class Decode_Model(BaseModel):
    author: str
    type: str
    message: str
    result: str
        
    class Config:
        schema_extra  = {
            "example": {
                "author": "sndyarzxch",
                "type": "base85",
                "message": "MQmwiX<;p6Xkl(4",
                "result": "Elifia-chan!",
            }
        }

def Encode(types, text):
    if types.lower() == "base64":
        res = str(byte.b64encode(text.encode("ascii")), "utf-8")
    elif types.lower() == "base32":
        res = str(byte.b32encode(text.encode("ascii")), "utf-8")
    elif types.lower() == "base16":
        res = str(byte.b16encode(text.encode("ascii")), "utf-8")
    elif types.lower() == "base85":
        res = str(byte.b85encode(text.encode("ascii")), "utf-8")
    else:
        res = "Invalid type baka!"
    return res

def Decode(types, text):
    try:
        if types.lower() == "base64":
            res = str(byte.b64decode(text.encode("ascii")), "utf-8")
        elif types.lower() == "base32":
            res = str(byte.b32decode(text.encode("ascii")), "utf-8")
        elif types.lower() == "base16":
            res = str(byte.b16decode(text.encode("ascii")), "utf-8")
        elif types.lower() == "base85":
            res = str(byte.b85decode(text.encode("ascii")), "utf-8")
        else:
            res = "Invalid type baka!"
    except:
        res = "It's not bytes code baka!" 
    return res
 