#importing libraries
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
import sys
import os
import random
import requests, json 

listener = sr.Recognizer()

def engine_talk(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def user_commands():
    try:
        with sr.Microphone() as source:
            engine_talk('hello i am alexa...how can i help you?')
            print("Start Speaking!!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
            print(command)
            return command
    except:
        command = "sorry"
        pass
        return command
    

def weather(city):
    # Enter your API key here 
    api_key = "06cd83676bd11d5b296484f92d4537d0"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    response = requests.get(complete_url) 
    x = response.json() 
    if x["cod"] != "404": 
        y = x["main"] 
        current_temperature = y["temp"] 
        temp_in_celcius = current_temperature - 273.15
        return str(int(temp_in_celcius))
    
def city_name():
    with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command

def run_alexa():
    command = user_commands()
    if 'name' in command:
        engine_talk("Hello! My  Name is Alexa")
    elif 'are you single' in command:
        answers = ['I am in a relationship with wifi','No, I love spending time thinking about my crush wifi']
        engine_talk(random.choice(answers))
    elif 'hate' in command:
        engine_talk("I hate when people called me a machine")
    elif 'love' in command:
        engine_talk("I love to chat with you")
    elif 'play a song' in command:
        song = 'Darshan Raval'
        engine_talk('Playing some music')
        print("Playing....")
        pywhatkit.playonyt(song)
    elif 'play' in command:
        song = command.replace('play', '')
        engine_talk('Playing....' + song)
        print("Playing....")
        pywhatkit.playonyt(song)     
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine_talk('Current Time is' + time)
    elif 'joke' in command:
        get_j = pyjokes.get_joke()
        print(get_j)
        engine_talk(get_j)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        engine_talk(info)
    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        engine_talk(info)
    elif 'weather' in command:
        engine_talk('Please tell name of the city')
        city = city_name()
        engine_talk('The temperature in ' +city + weather(city) + 'degree celcius')
    elif 'stop' in command:
        engine_talk("Good Bye...Have a nice day!")
        sys.exit()
    else:
        engine_talk("I didn't hear you properly")
        print("I didn't hear you properly")

while True:
    run_alexa()