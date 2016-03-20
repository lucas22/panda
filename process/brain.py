import inout.speech as speech
import settings
import os

# map keywords to group of actions
def interpret (words):
    action = None
    for w in words:
        i = words.index(w)+1
        action = map(w)
        if action is not None:
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
            if action is "telljoke":
                speech.telljoke()

def a_browse (i, words):
    website = ''.join(words[i:]) + ".com"
    os.system("sensible-browser " + website)

def a_search (i, words):
    term = words[i:]
    query = settings.cfg['web']['search_engine_query'] + "+".join(term)
    os.system("sensible-browser " +  query)

def a_define (i, words):
    if "your"
    if "time" in words:
        speech.read_text( "Now it is " + speech.current_time() )
    else:
        term = words[i:]
        query = settings.cfg['web']['search_engine_query'] + "define:" + "+".join(term)
        os.system("sensible-browser " + query)

def a_speak (i, words):
    text = ' '.join(words[i:])
    speech.read_text(text)

def map (word):
    for k in settings.keywords:
        if word in settings.keywords[k]:
            #print (word + " >> " + str(k))
            return k
    return None
