import general_conversations
import re
import os

def brain(name, speech_text):
    def check_message(check):
        words_of_meaning = speech_text.split()
        if set(check).issubset(set(words_of_meaning)):
            return True
        else:
            return False
            
    if check_message(['alarm']) or check_message(['wake']):
        time = re.findall('\d+', speech_text)
        os.environ["hour"] = time[0]
        os.environ["minute"] = time[1]
        general_conversations.alarm()
    if check_message(['what','time']):
        general_conversations.what_isthe_time()
    if check_message(['what','weather']) or check_message(['how','weather']):
        words_of_meaning = speech_text.split()
        place = words_of_meaning[len(words_of_meaning)-1]
        general_conversations.what_isthe_weather(place)
    if check_message(['what','date']):
        general_conversations.what_isthe_date()
    if check_message(['who','are','you']):
        general_conversations.who_are_you()
    elif check_message(['how', 'I', 'look']) or check_message(['how', 'am', 'I']):
        general_conversations.how_am_i()
    elif check_message(['tell', 'joke']):
        general_conversations.tell_joke()
    elif check_message(['who', 'am', 'I']):
        general_conversations.who_am_i(name)
    elif check_message(['where', 'born']):
        general_conversations.where_born()
    elif check_message(['how', 'are', 'you']):
        general_conversations.how_are_you()
    elif check_message(['exit']):
        general_conversations.exiting()
    else:
        general_conversations.undefined()
