import os
import time
import webbrowser
import random
import urllib.request  as urllib2
from bs4 import BeautifulSoup
import pyglet
from gtts import gTTS
from weather import Weather

def tts(text):
    tts = gTTS(text=text, lang='en-uk',slow=False )
    tts.save('..\Sherley\hello.mp3')
    music = pyglet.media.load('..\Sherley\hello.mp3', streaming=False)
    music.play()

    time.sleep(music.duration) #prevent from killing
    os.remove('..\Sherley\hello.mp3') #remove temperory file
    
def alarm(hour, minute):
    while 1:
        timing = time.localtime()
        time.sleep(10)
        if(timing.tm_hour == hour and timing.tm_min == minute):
            tts('Good morning jersha wake up, its'+str(timing.tm_hour)+str(timing.tm_min))
            time.sleep(30)
            
            wtr = Weather()
            location = wtr.lookup_by_location('bangalore')
            condition = location.condition()
            tts('The weather is '+condition['text']+' and the temperature is '+(str((int(condition['temp'])-32)*0.6))+' degree celcius')
            time.sleep(30)
            
            urls = []
            textToSearch = ['vidyavox','dilton pagal hai','kuch kuch hota hai songs','premam songs']
            query = urllib2.quote(random.choice(textToSearch))
            url = "https://www.youtube.com/results?search_query=" + query
            response = urllib2.urlopen(url)
            html = response.read()
            soup = BeautifulSoup(html)
            for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
                urls.append('https://www.youtube.com' + vid['href'])
            webbrowser.open(random.choice(urls))
            break
        
alarm(int(os.environ["hour"]),int(os.environ["minute"]))



