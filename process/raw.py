import brain


# start request processing
def process(request):
    request = normalize(request)
    words = tokenize(request)
    brain.interpret(words)


# normalize request
def normalize(request):
    request = request.lower()
    return request


# create tokens
def tokenize(request):
    words = request.split()
    return words
