import tempfile
import sounddevice as sd
from scipy.io.wavfile import write
import pyttsx3

def record_audio(seconds=5):
    fs = 16000
    data = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    fp = tempfile.mktemp(".wav")
    write(fp, fs, data)
    return fp

class TTS:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
