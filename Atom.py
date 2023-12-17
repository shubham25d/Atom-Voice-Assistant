import datetime
from http import server
import time
from logging import exception
import pyttsx3 
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib 
import pywhatkit as pwt
import os
import playsound
import subprocess
import urllib.request
import re

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices) 
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")  

    elif hour>=12 and hour<18:
        speak("Good after noon")

    else:
        speak("Good Evening")

    speak("Atom here. How may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)

        
    try:
        print("Processing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query



def sendEmail(to, content):
          
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('shubhamdhakate25@gmail.com', 'ssd25807')
        server.sendmail('shubhamdhakate25@gmail.com', to, content)
        server.close()
    
    except:
        print("error")
  
if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia.') 
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('Opening Youtube')
        
        elif 'open google' in query:
            webbrowser.open("google.com")
            print("Opening google")
            speak('Opening Google')

        elif 'open email' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak('Opening Email Inbox')

        elif 'open inbox' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak('Opening Email Inbox')

        elif 'who are you' in query:
            speak('I am A virtual assitant')        

        elif 'Open calculator' in query:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            speak('Opening Calculator')

        elif 'Open Notepad' in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
            speak('Opening Notepad')

        elif 'Open Teams' in query:
            subprocess.Popen('C:\\Windows\\System32\\Teams.exe')
            speak('Opening Microsoft Teams')

        elif 'Open Camera' in query:
            subprocess.Popen('C:\\Windows\\System32\\camera.exe')
            speak('Opening Camera. Smile Please!')

        elif 'Open Application' in query:
            speak('Which app do you want to open?')
            content=takeCommand()
            subprocess.Popen('C:\\Windows\\System32\\'+(content)+'.exe')
            speak('Opening Camera. Smile Please!')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {strTime}")   


        elif 'search on youtube' in query:
            speak("Ok, What do you want to see in youtube")
            content=takeCommand()
            search_keyword = "..."  
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + content)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            pwt.search("https://youtube.com/watch?v=" + video_ids[0])

        
        elif 'set alarm' in query:
            speak('What hour do you want to wake up?')
            content=takeCommand()
            speak('What Minute do you want to wake up?')
            content2=takeCommand()
            speak('am or pm')
            content3=takeCommand()
           

            if (content3 == "pm"):
               content = content2 + 12

            while(1 == 1):
                if(content == datetime.datetime.now().hour and
                    content2 == datetime.datetime.now().minute):
                    speak('Time Up.Time Up.Time Up.Time Up.Time Up.Time Up.Time Up.Time Up.Time Up.Time Up.Time Up.Time Up.Time Up.Time Up.Time Up.Time Up.')

             
        
        elif 'email bhavana' in query:
            try:
                speak("Ok, What should I say?")
                content = takeCommand()
                to = "bhavanadhakate22@gmail.com"
                sendEmail(to, content)
                speak("Email has been Sent!")
            except Exception as e:
                print(e)
                speak("Error occured in sending this email...")

        elif 'email suhas' in query:
            try:
                speak("Ok, What should I say?")
                content = takeCommand()
                to = "suhasdhakate@gmail.com"
                sendEmail(to, content)
                speak("Email has been Sent!")
            except Exception as e:
                print(e)
                speak("Error occured in sending this email...")

        elif 'email shubham' in query:
            try:
                speak("Ok, What should I say?")
                content = takeCommand()
                to = "shubhamdhakate25@gmail.com"
                sendEmail(to, content)
                speak("Email has been Sent!")
            except Exception as e:
                print(e)
                speak("Error occured in sending this email...")


        


        elif 'google search' in query:
            try:
                speak('What should I search?')
                content=takeCommand()
                pwt.search(content)

            except:
                speak("Atom Not responding!")

#.....OPTION-2(ALARM)
        #elif 'Set alarm' in query:

           #from playsound import playsound
           #from AppKit import NSSound
           #os. system('clear')
           #alarmH = int(takecommand()("What hour do you want the alarm to ring? "))
           #alarmM = int(takecommand()("What minute do you want the alarm to ring? "))
           #amPm = str(query("am or pm? "))
           #os. system('clear')
           #print("Waiting for alarm",alarmH,alarmM,amPm)
           #if (amPm == "pm"):
           #        alarmH = alarmH + 12
           #while(1 == 1):
           #    if(alarmH == datetime.datetime.now().hour and
           #        alarmM == datetime.datetime.now().minute) :
           #       speak("Time up")
        #          speak("TINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTINGTING")                    
           #       break       
            



   