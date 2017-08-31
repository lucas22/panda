from gtts import gTTS
from tempfile import *
from datetime import datetime
import deps.vlc as vlc
import settings as s
import random
import time
import os


def ty_resp():
    say(random.choice(s.ty_resp))


def greeting():
    say(random.choice(s.greetings['long']))


def tell_joke():
    say(random.choice(s.jokes))


def current_time():
    t = datetime.now().strftime("%I:%M %p")
    return t

def close():
    say('See you later')
    exit(0)

def say(text_to_read):

    # s.no_ears()

    # get audio
    tts = gTTS(text=text_to_read, lang='en')
    f = NamedTemporaryFile(delete=False, prefix="tts", suffix=".mp3")
    tts.write_to_fp(f)
    f.close()

    # play audio
    v = vlc.MediaPlayer(f.name)
    v.play()

    # clean up
    while True:
        time.sleep(1)
        if not ( v.get_state() is "State.Playing" or v.get_state() is "State.Opening" ):
            os.system("rm " + f.name)
            break;

    # restart listening
    #s.listen_to_me()
