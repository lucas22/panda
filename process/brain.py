import commands
import inout.speech as speech
import settings
import os

# map keywords to group of actions
def sys_update():
    output = commands.getstatusoutput("apt update && apt upgrade")
    error = output[0]
    if not error:
        speech.say("System up-to-date")
    else:
        speech.say("Error updating")
    print (output[1])

# interpret action words
def interpret(words):
    for w in words:
        i = words.index(w) + 1
        action = map_word_to_action(w)
        if action is not None:
            if action is "greeting":
                speech.greeting()
            if action is "browse":
                a_browse(i, words)
            if action is "search":
                a_search(i, words)
            if action is "define":
                a_define(i, words)
            if action is "speak":
                a_speak(i, words)
            if action is "ty_resp":
                speech.ty_resp()
            if action is "tell_joke":
                speech.tell_joke()
            if action is "update":
                sys_update()
            if action is "close":
                speech.close()


def a_browse(i, words):
    website = ''.join(words[i:]) + ".com"
    os.system("sensible-browser " + website)


def a_search(i, words):
    term = words[i:]
    query = settings.cfg['web']['search_engine_query'] + "+".join(term)
    os.system("sensible-browser " + query)


def a_define(i, words):
    if "time" in words:
        speech.say("Now it is " + speech.current_time())
    else:
        term = words[i:]
        query = settings.cfg['web']['search_engine_query'] + "define:" + "+".join(term)
        os.system("sensible-browser " + query)


def a_speak(i, words):
    text = ' '.join(words[i:])
    speech.say(text)


def map_word_to_action(word):
    for k in settings.keywords:
        if word in settings.keywords[k]:
            # print (word + " >> " + str(k))
            return k
    return None
