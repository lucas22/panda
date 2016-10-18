import speech_recognition as sr
import process.raw as p
import sys


def listen(recognizer, audio):
    try:
        request = recognizer.recognize_google(audio, language="en-US")
        print("\nI heard: " + request)
    except sr.UnknownValueError:
        sys.stdout.write(". ")
        sys.stdout.flush()
        return
    except sr.RequestError as e:
        print("Error listening: {0}".format(e))
        return

    p.process(request)
