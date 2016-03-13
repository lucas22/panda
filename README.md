# PANDA - Personal Automated Non-Deterministic Assistant

### Dependencies:
* [Python](https://www.python.org)
* [SpeechRecognition](https://pypi.python.org/pypi/SpeechRecognition)
* [gTTS](https://pypi.python.org/pypi/gTTS)
* [VLC](https://wiki.videolan.org/Python_bindings)

### Directory structure:
``` c
├- panda                   # root directory
│   ├- deps                    # dependencies
│   │   ├- vlc.py                  # third party module to play media
│   ├- text                    # text files
│   │   ├- domains.txt             # set of familiar domains
│   ├- io                      # input/output files
│   │   ├- ears.py                 # audio input
│   │   ├- speech.py               # audio output
│   ├- process                 # processing
│   │   ├- raw.py                  # initial input processing
│   ├- panda                   # executable
│   ├- panda.config            # configuration file
```
