import inout.speech as speech
import settings as s
import os
import sys

# start request processing
def process (request):
    request = normalize(request)
    words = tokenize(request)
    interpret(words)

# normalize request
def normalize (request):
    request = request.lower()
    return request

# create tokens
def tokenize (request):
    words = request.split()
    return words

# analyze tokens (words) and take action
def interpret (words):
    if ( words[0] == "time" ):
        speech.read_text( "Now it is " + speech.current_time() )

    if ( len(words)>1 and words[0] == "open" ):
        website = None
        if ( words[1] == "my" and words[2] == "website" ):
            website = s.cfg['web']['personal_website']
        elif ( words[1] == "facebook" ):
            website = words[1] + ".com"
        if (website is not None):
            os.system("sensible-browser " + website)
    elif ( words[0] == "search" ):
        os.system("sensible-browser " + s.cfg['web']['search_engine_query'] + "+".join(words[1:]) )
    elif ( words[0] == "repeat" or words[0] == "say"):
        speech.read_text( ' '.join(words[1:]) )
    elif ( words[0] == "dammit" and words[1] == "chloe"):
        speech.read_text( "Sorry, Jack. I'm doing my best here!" )
