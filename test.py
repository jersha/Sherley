from pubnub.callbacks import SubscribeCallback 
from pubnub.enums import PNStatusCategory  
from pubnub.pnconfiguration import PNConfiguration  
from pubnub.pubnub import PubNub, SubscribeListener

pnconfig = PNConfiguration() 

pnconfig.subscribe_key = "sub-c-4191c43e-8002-11e7-8979-5e3a640e5579" 
pnconfig.publish_key = "pub-c-c8c32aba-5b66-467d-8c15-1663497b3b32" 
pnconfig.uuid = "UUID-Sherley"

pubnub = PubNub(pnconfig)

my_listener = SubscribeListener()
pubnub.add_listener(my_listener)

def callback(message, channel):
    print(message)

def error(message):
    print("ERROR : " + str(message))

def connect(message):
    print("CONNECTED")
    


def reconnect(message):
    print("RECONNECTED")


def disconnect(message):
    print("DISCONNECTED")

channel = "My-Location"

def my_publish_callback(envelope, status):
  print(envelope, status)

pubnub.subscribe(channel=channel, callback=callback, error=callback,
                 connect=connect, reconnect=reconnect, disconnect=disconnect)

pubnub.publish().channel("My-Location").message("jersha u r awesome").async(my_publish_callback)

pubnub.subscribe().channel("My-Location").async(callback).execute()
