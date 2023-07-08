import pyttsx3
import speech_recognition as sr

class VoiceSupport:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()

    def text_to_speech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def speech_to_text(self, speech):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
            text = self.recognizer.recognize_google(audio)
            return text