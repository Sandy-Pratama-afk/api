#hello><
import re, random
from pydantic import BaseModel

class Reply_Model(BaseModel):
    author: str
    message: str
    result: str
        
    class Config:
        schema_extra  = {
            "example": {
                "author": "sndyarzxch",
                "message": "Hi",
                "result": "Hallo ><",
            }
        }
        
def Reply(text: str):
    if re.findall("he.+o|ha.+o|hi|h.+i", text.lower()):
        return random.choice(["Hallo!!", "Haii!!", "Yahallooo!!", "Hello ><", "Hiii><", "Haii ayang><"])
    elif re.findall("siapa nama kamu|nama kamu siapa|siapa namamu|namamu siapa|namamu", text.lower()):
        return random.choice(["Haii namaku Elifia!", "Nama aku Elifia ><", "Hello, aku Elifia!", "Namaku Elifia"])
    elif re.findall("pacarmu|pacar kamu", text.lower()):
        return random.choice(["Pacarku? Mmmm ... I-1tu k-kamu ><", "Sandy-kun ><", "Hmmm, kalau kamu mau ngga jadi pacar Elifia??", "Hmmm ... Siapa ya?"])
    else:
        return "Humm?"