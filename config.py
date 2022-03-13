import logging
import os
from logging.handlers import RotatingFileHandler




TG_BOT_TOKEN = "5176557616:AAG0GACYWHwaAMoJGA7SgArabLpTsgWAEvA"
#OWNER_ID = "1393311560"
ADMINS = list(set(int(x) for x in ("1393311560").split(" ")))
APP_ID = "11935084"
API_HASH = "644b5ad6ad0e5d394cfe6b780f47680c"
TG_BOT_WORKERS = int(4)


FORCE_SUB_CHANNEL = list(set(int(x) for x in ("-1005176557616 -1001698176510").split(" ")))
FORCE_SUB_GROUP = list(set(int(x) for x in ("-1001698176510").split(" ")))
PICS = "https://telegra.ph/file/03f521347213efc715449.jpg"
OTHER_BOT_1 = ""


CHANNEL_ID = int(-1001567372048)
DB_URI = "postgres://cojeankhwfurer:f56958ab3ebe67722c2e679d3e7a5abc9b1f86a6a93f63d57dfa8eaeb49acd96@ec2-52-44-209-165.compute-1.amazonaws.com:5432/dcc5ildjmgf2i"


CAPTION_ABOUT_PHOTO = "https://telegra.ph/file/7c5c0dc8ee6723aac16be.jpg"
CAPTION_CLOSE_PHOTO = "https://telegra.ph/file/03f521347213efc715449.jpg"


POST_CAPTION = f"""
<a href='https://t.me/viralmerahmuda'>
<b>🚨 WARNING 🚨<i>


🔰 Konten ini hanya untuk pemuas nafsu
🔰 Menontonlah secukupnya, bikin kecanduan
🔰 ENJOY FOR WATCHING VIDEOS❗️</i></b></a>


@viralmerahmudabot @viralmerahmuda
#viral
#indo
"""

CAPTION_CLOSE = f"""
Bye...
"""

CAPTION_ABOUT = f"""
kintill...
"""

START_MSG = f"""
<b>Hello ,
Saya dapat menyimpan file pribadi di Channel Tertentu dan pengguna lain dapat mengaksesnya dari link khusus.</b>

"""

FORCE_MSG = f"""
<b>Hello, 
Anda harus join dulu untuk menggunakan saya

"""

CUSTOM_CAPTION = f"""
<i><a href ='https://t.me/viralmerahmuda'>📌 Terus dukung channel ini agar mimin semangat update 👌</a></i>

<b>@viralmerahmuda @viralmerahmuda
#viral 
#merah 
#muda</b>

"""



LOG_FILE_NAME = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
