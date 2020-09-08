
import datetime
import os
import smtplib
import webbrowser
import pyaudio
import pyttsx3
import speech_recognition as sr
import wikipedia
import subprocess
import requests
import json

print("siri initalizing")
MASTER = "sir"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
#speaking function
def speak(text):
    engine.say(text)
    engine.runAndWait()

#wishing function as per time 
def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("good morning" + MASTER)
    elif hour>=12 and hour<18:
         speak("good afternoon" + MASTER)
    else:
         speak("good evening" + MASTER)

    speak("i am siri. How  can i help you ? ")  
#this function takes commands from microphone
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e :
        print("say that again unable to recognize")
        query = None
    return query
def weather():
    api_key = "f23271ea9133c4ce363d7590c5b70950"
  

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
  

    city_name = input("Enter city name : ") 
  

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
  

    response = requests.get(complete_url) 
  

    x = response.json() 
  
    if x["cod"] != "404":  
        y = x["main"] 
        current_temperature = y["temp"]  
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"] 
        z = x["weather"] 
        weather_description = z[0]["description"] 
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) + 
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidiy) +
            "\n description = " +
                        str(weather_description)) 
    
    else: 
        print(" City Not Found ") 

#main function starts here
speak("hello")
wishme()
query = takeCommand()

if 'wikipedia' in query.lower():
    speak('searching wikipedia...')
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences = 2)
    print(results)
    speak (results)
elif 'open youtube' in query.lower():
    url = "youtube.com"
    webbrowser.open("youtube.com")
elif ('mail' or 'gmail') in query.lower():
    url = "gmail.com"
    webbrowser.open("gmail.com")
elif 'open google' in query.lower():
    url = "google.com"
    webbrowser.open("google.com")
elif 'play music' in query.lower():
    songs_dir= "C:\\Users\\LIGION\\Desktop\\music"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))
elif 'the time' in query.lower():
    strTime  = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strTime}")
elif ("multiply" or "divide" or "add" or "subtraact") in query.lower():
    subprocess.Popen('C:\\Windows\\System32\\calc.exe')

elif ('climate' or 'weather' or 'climatic') in query.lower():
    api_key = "f23271ea9133c4ce363d7590c5b70950"
  

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
  

    city_name = input("Enter city name : ") 
  

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
  

    response = requests.get(complete_url) 
  

    x = response.json() 
  
    if x["cod"] != "404":  
        y = x["main"] 
        current_temperature = y["temp"]  
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"] 
        z = x["weather"] 
        weather_description = z[0]["description"] 
        print(" Temperature (in kelvin unit) = " +
                        str(current_temperature) + 
            "\n atmospheric pressure (in hPa unit) = " +
                        str(current_pressure) +
            "\n humidity (in percentage) = " +
                        str(current_humidiy) +
            "\n description = " +
                        str(weather_description)) 
    
    else: 
        print(" City Not Found ")   

