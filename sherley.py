import speech_recognition as sr
import brain
from subprocess import Popen

r = sr.Recognizer()
with sr.Microphone() as source:
    while 1:
        audio = r.listen(source)
        try:
            brain.brain("Jersha", r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service;{0}".format(e))



