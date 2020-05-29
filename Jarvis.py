import speech_recognition as sr
import webbrowser as wb
import os
from gtts import gTTS
import wikipedia
import datetime
import calendar
import random
import warnings

user_name = 'Priya'

def my_request():
    question = 'hey Jarvis! Who is Narendra Modi?'
    speech = gTTS(text=question, lang='en', slow=False)
    speech.save("my_query.wav")

def speech_recognition_module():
    rec = sr.Recognizer()
    audio = sr.AudioFile('transcript.mp3')
    print('Speak Now')
    with audio as source:
        audio = rec.record(source)
        try:        
            text = rec.recognize_google(audio, language='en-US', show_all=True)
            print(text)
            return text['alternative'][0]['transcript']
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None


def speech_recognition_module_silence():
    pass

def text_to_speech_module(text, lang):
    speech = gTTS(text=text, lang=lang, slow=False)
    speech.save("assistant_response.wav")
    os.system("assistant_response.wav") 

def wake_word(text):
    wake_words = ['hey jarvis', 'jarvis']
    text = text.lower()
    for phrase in wake_words:
        if phrase in text: return True
    return False

def greetings(text):
    greetings = ['hi', 'hello', 'namaste', 'good morning', 'good afternoon', 'good evening']
    greetings_response = ['hi', 'hello', 'namaste', 'hey there', 'howdy']
    text = text.lower()
    for phrase in greetings:
        if phrase in text: return random.choice(greetings_response) + user_name + '.'
    return ''

def get_particulars(text):
    word_list = text.split()
    particulars = ''
    for i in range(len(word_list)):
        print(particulars)
        if i+2<=len(word_list)-1 and (word_list[i].lower()=='who' or word_list[i].lower()=='what') and word_list[i+1].lower()=='is':
            for j in range(i+2, len(word_list)):
                particulars += word_list[j]
            break
    return particulars

def assistant_response(text, lang):
    response = ''
    if wake_word(text)==True:
        response += greetings(text)
        if 'who is' or 'what is' in text:
            particulars = get_particulars(text)
            wiki = wikipedia.summary(particulars, sentences=2)
            print(wiki)
            response += (' ' + wiki)
        if response=='':
            response = greetings('hi')
        text_to_speech_module(response, lang)

def transcript():
    rec = sr.Recognizer()
    audio = sr.AudioFile('sample4.wav')
    print('Speak Now')
    with audio as source:
        audio = rec.record(source)
        try:        
            text = rec.recognize_google(audio, language='en-US', show_all=True)
            transcripts = []
            for i in range(5):
                transcripts.append(text['alternative'][i]['transcript'])
            return transcripts
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None
        
#text_to_speech_module('Hi'+ user_name +'. How can I help you?', 'en')
#assistant_response(speech_recognition_module(),'en') 

#my_request()
#assistant_response(speech_recognition_module(), 'en')
#assistant_response('hi jarvis what is coronavirus', 'en')

trs = transcript()
print(trs)
#speech_recognition_module()