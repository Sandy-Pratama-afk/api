import re
from fastapi import FastAPI, APIRouter, HTTPException, Request
#from fastapi.templating import Jinja2Templates
#from pathlib import Path
from typing import Optional
from lib.Say import Reply, Reply_Model
from lib.Hash import Hashing, Hashing_Model
from lib.Bytes import Encode, Decode, Encode_Model, Decode_Model
from lib.Loli import Loli, Loli_Model
from lib.YouTube import Audio, Video, Y_Model

APP = FastAPI(title="Sndyarzxch API",
              version="0.0.1",
              openapi_url="/openapi.json")
ROUTER = APIRouter()
#BASE_PATH = Path(__file__).resolve().parent
#TEMPLATES = Jinja2Templates(directory=str(BASE_PATH / "web"))

@ROUTER.get("/", status_code=200)
def root(request: Request) -> dict:
    """
    Home API
    """
    return {
        "author": "sndyarzxch",
        "detail": "Looking for what?",
        "docs": [
            "/say?text=helo Mengirimkan response teks kamu (beta)",
            "/hash?algo=algo&text=text Hashing your text with sha1, sha224, sha256, sha512, or md5",
            "/encode?text=text Encode your text to base16, base32, base64, or base85",
            "/decode?text=text Decode your text from base16, base32, base64, or base85",
            "/loli Return random loli images ><",
            "/ytmp4?url=url YouTube video downloader (720p)",
            "/ytmp3?url=url YouTube audio downloader (128k)"
        ]
    }
#    return TEMPLATES.TemplateResponse(
#        "index.html", 
#        {"request":request})

@ROUTER.get("/say", status_code=200, response_model=Reply_Model)
def say_your_text(text: Optional[str] = None) -> dict:
    """
    Mengirimkan response teks!
    """
    if not text:
        raise HTTPException(status_code=404, detail="Example parameter: /say?text={text} baka!")
    res = Reply(text)
    return {
        "author": "sndyarzxch",
        "message": text,
        "result": res
    }

@ROUTER.get("/hash", status_code=200, response_model=Hashing_Model)
def hashing_generator(algo: Optional[str] = None, text: Optional[str] = None) -> dict:
    """
    Hash generator
    """
    if not algo or not text:
        raise HTTPException(status_code=404, detail="Example parameters: /hash?algo={algo}&text={text} baka!")
    res = Hashing(algo, text)
    return {
        "author": "sndyarzxch",
        "algorithm": algo.upper(),
        "message": text,
        "result": res
    }

@ROUTER.get("/encode", status_code=200, response_model=Encode_Model)
def Bytes_encoder(type: Optional[str] = None, text: Optional[str] = None) -> dict:
    """
    Bytes encode
    """
    if not type or not text:
        raise HTTPException(status_code=404, detail="Example parameters: /encode?type={type}&text={text} baka!")
    return {
        "author": "sndyarzxch",
        "type": type,
        "message": text,
        "result": Encode(type, text)
    }

@ROUTER.get("/decode", status_code=200, response_model=Decode_Model)
def Bytes_decoder(type: Optional[str] = None, text: Optional[str] = None) -> dict:
    """
    Bytes decode
    """
    if not type or not text:
        raise HTTPException(status_code=404, detail="Example parameters: /decode?type={type}&text={text} baka!")
    return {
        "author": "sndyarzxch",
        "type": type,
        "message": text,
        "result": Decode(type, text)
    }

@ROUTER.get("/loli", status_code=200, response_model=Loli_Model)
def random_loli_images() -> dict:
    """
    Random loli images
    """
    return {
        "author": "sndyarzxch",
        "result": Loli()
    }

@ROUTER.get("/ytmp4", status_code=200, response_model=Y_Model)
def YouTube_video_downloader(url: Optional[str] = None) -> dict:
    """
    YouTube Video Downloader
    """
    if not url or not re.findall("youtu.be|youtube.com/watch", url):
        raise HTTPException(status_code=404, detail="Invalid url baka!")
    return Video(url)

@ROUTER.get("/ytmp3", status_code=200, response_model=Y_Model)
def YouTube_audio_downloader(url: Optional[str] = None) -> dict:
    """
    YouTube Audio Downloader
    """
    if not url or not re.findall("youtu.be|youtube.com/watch", url):
        raise HTTPException(status_code=404, detail="Invalid url baka!")
    return Audio(url)

APP.include_router(ROUTER)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(APP, host="0.0.0.0", port=1605, log_level="debug")