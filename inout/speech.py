from gtts import gTTS
from tempfile import *
from datetime import datetime
import deps.vlc as vlc
import os

def current_time():
    t = datetime.now().strftime("%I:%M %p")
    return t

def read_text(text_to_read):
    tts = gTTS(text=text_to_read, lang='en')
    f = NamedTemporaryFile(delete=False, prefix="tts", suffix=".mp3")
    tts.write_to_fp(f)
    f.close()

    v = vlc.MediaPlayer(f.name)
    v.play()
    os.system("rm " + f.name)
