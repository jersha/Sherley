import speech_recognition as sr
import pyttsx
engine = pyttsx.init()
engine.say('Good morning.')
engine.runAndWait()

#r = sr.Recognizer()
#with sr.Microphone() as source:
#    print("say something")
#    audio = r.listen(source)
#    
#try:
#    print("google speech recognition thinks you said "+r.recognize_google(audio))
#except sr.UnknownValueError:
#    print("Google Speech Recognition could not understand audio")
#except sr.RequestError as e:
#    print("Could not request results from Google Speech Recognition service;{0}".format(e))
#
#with open("recording.wav", "wb") as f:
#    f.write(audio.get_wav_data())


