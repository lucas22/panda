import speech_recognition as sr
import inout.speech as speech
import inout.ears as ears
import ConfigParser
import sys
import os

def config():
    load_config()
    load_vars()


def load_config():
    panda_config = ConfigParser.ConfigParser()
    global cfg
    cfg = {}

    def get_setts_by_section(section):
        settings = {}
        opts = panda_config.options(section)
        for o in opts:
            try:
                settings[o] = panda_config.get(section, o)
                if (settings[o] == -1):
                    print ("error balalaika")
            except:
                print("exception on setting: %s" % o)
                settings[o] = None
        return settings

    panda_config.read("panda.config")
    cfg['gen'] = get_setts_by_section("General")
    cfg['web'] = get_setts_by_section("Web")


def load_vars():
    global keywords, greetings, ty_resp, jokes

    keywords = {'browse': ['browse', 'open', 'visit'], 'search': ['search', 'google'], 'define': ['define', 'what'],
                'speak': ['say', 'repeat', 'shout', 'speak'], 'ty_resp': ['thanks', 'thank'],
                'tell_joke': ['joke', 'jokes'], 'greeting': ['hi', 'hello', 'greetings'],
                'update': ['update', 'upgrade']}

    greetings = {'long': ["Hello, how are you today?", "Hi there, " + cfg['gen']['user_name']],
                 'short': ["Hello", "Hi there", "Greetings"]}

    ty_resp = ["you are welcome", "it's nothing", "it's my pleasure"]

    jokes = [
        "What is the difference between a large pizza and a professional online poker player? The large pizza can feed a family of four",
        "I keep hitting \"escape\", but I'm still here.", "Your life"]


def start_assistant():

    ret = os.system("jack_control start")
    if ret:
        exit(2)

    speech.greeting()
    listen_to_me()

    while True:
        msg = sys.stdin.readline()
        speech.say(msg)


def listen_to_me():
    r = sr.Recognizer()
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

    global stop_listening
    stop_listening = r.listen_in_background(source, ears.listen)


def no_ears():
    global stop_listening
    stop_listening()