import random
import time
from gtts import gTTS
from pygame import mixer
import os
import pyglet
from subprocess import Popen
from subprocess import call
import datetime
from weather import Weather

def tts(text):
    tts = gTTS(text=text, lang='en-uk',slow=False )
    tts.save('..\Sherley\hello.mp3')
    music = pyglet.media.load('..\Sherley\hello.mp3', streaming=False)
    music.play()

    time.sleep(music.duration) #prevent from killing
    os.remove('..\Sherley\hello.mp3') #remove temperory file
def what_isthe_time(place):
    timing = time.localtime()
    message = 'time is'+str(timing.tm_hour)+str(timing.tm_min)
    tts(message)
def what_isthe_weather(place):
    wtr = Weather()
    location = wtr.lookup_by_location(place)
    if(location == None):
        tts('please be specific')
    else:
        condition = location.condition()
        tts('The weather is '+condition['text']+' and the temperature is '+(str((int(condition['temp'])-32)*0.6))+' degree celcius')
def what_isthe_time():
    timing = time.localtime()
    message = 'time is'+str(timing.tm_hour)+str(timing.tm_min)
    tts(message)
def what_isthe_date():
    dt = datetime.datetime.now()
    message = 'date is day '+str(dt.day)+' month '+str(dt.month)+' year '+str(dt.year)
    tts(message)
def alarm():
    message = 'alarm set to'+os.environ["hour"]+os.environ["minute"]
    tts(message)
    Popen('python Alarm.py')
def who_are_you():
    messages = ['I am sherley, your poetic personal assistant','Sherley, i think i told you before itself?','You ask that so many times! I am Sherley.']
    tts(random.choice(messages))
def how_am_i():
    replies =['You are goddamn handsome!', 'My knees go weak when I see you.','You are sexy!', 'You look like the kindest person that I have met.']
    tts(random.choice(replies))
def tell_joke():
    jokes = ['What happens to a frogs car when it breaks down? It gets toadaway.', 'Why was six scared of seven? Because seven ate nine.', 'No, Ialways forget the punch line.']
    tts(random.choice(jokes))
def who_am_i(name):
    tts('You are ' + name + ', an awesome person. I love you!')
def where_born():
    tts('I was created by a magician named Jersha, in India, the magical landof beautiful girls.')
def how_are_you():
    tts('I am fine, thank you.')
def undefined():
    print('didnt understand')
def exiting():
    exit()


