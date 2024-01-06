import datetime    
import pyttsx3
import speech_recognition as sr
import wikipedia
import os
import webbrowser as wb
import random
import subprocess
from validateEmail import validate
from NetworkSpeed import speedTest
from GenerateStrongPassword import passGen
from youtubeVideoDownload import downloadVideo

try:
    from googlesearch import search
except ImportError: 
    print("No module named \'google\' found")

wb = wb.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',230) 

r = sr.Recognizer()
m = sr.Microphone()

sites = [
    ["youtube","youtube.com"],
    ["google","google.com"],
    ["chrome","google.com"],
    ["instagram","instagram.com"],
    ["facebook","facebook.com"],
    ["leetcode","leetcode.com"],
    ["lead code","leetcode.com"],
    ["leadcode","leetcode.com"],
    ["leadcode","leetcode.com"],
    ["wikipedia","wikipedia.org"]
]

apps = [
    ["x mind","C:\\Users\\anvit\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Xmind.lnk"],
    ["vscode","C:\\Users\\anvit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"],
    ["visual studio","C:\\Users\\anvit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"],
    ["code","C:\\Users\\anvit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"],
    ["craft","C:\\Users\\anvit\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Craft.lnk"],
    ["edge","C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk"],
    ["microsoft browser","C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk"],
    ["figma","C:\\Users\\anvit\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Figma.lnk"],
]

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def welcome():
    hour = int(datetime.datetime.now().hour)
    if hour>=12 and hour<17 :
        speak("Good Afternoon Sir")
    elif hour>=17 and hour<21 :
        speak("Good Evening Sir")
    else :
        speak("Good Morning Sir")
    speak("I am Jarvis, ready for help")

def listen():
        with m as source :
            print("Listening...")
            r.pause_threshold = 1 
            r.energy_threshold = 600
            audio = r.listen(source)
        try :
            print("Recognising")
            query = r.recognize_google(audio,language='en-us')
        except Exception as e:
            engine.setProperty('rate',190)
            speak("Network Request error")
            speak("Please restart again")
            engine.setProperty('rate',230)
            return ""
        return query

def command():
    while(1):
        query = listen()
        query = query.lower()
        print(query)
        
        if "jarvis" in query:
            query = query.replace("jarvis","")

            if ("how are you" in query) or ("are u ok" in query) or ("are you ok" in query) or ("how r u" in query) or ("hello" in query):
                speak("I am fine sir, waiting for you, to give me some work")
        
            elif ("internet" in query) or ("wikipedia" in query) :
                query = query.replace("internet"," ")
                engine.setProperty('rate',190)
                # wikipedia.set_lang("hi")
                result = wikipedia.summary(query,sentences=2)
                print(result)
                speak(result)
                engine.setProperty('rate',230)
                
            elif "open" in query: 
                for app in apps :
                    if app[0] in query :
                        engine.setProperty('rate',190)
                        speak(f"opening {app[0]}")
                        engine.setProperty('rate',230)
                        os.startfile(app[1])

                for site in sites :
                    if site[0] in query:
                        engine.setProperty('rate',190)
                        speak(f"Opening {site[0]}")
                        engine.setProperty('rate',230)
                        wb.open_new(site[1])    

            elif "lock device" in query:
                cmd='rundll32.exe user32.dll, LockWorkStation'
                subprocess.call(cmd)

            elif "sleep device" in query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  
            
            elif ("shutdown device" in query) or ("shut down device" in query):
                os.system("shutdown /s /t 1")

            elif ("restart device" in query) :
                os.system("shutdown /r /t 1")

            elif ("log out from device" in query) or ("logout" in query):
                os.system("shutdown -l")
                
            elif "play movie" in query :
                movie_dir = "C:\\Users\\anvit\\Videos\\Movies"
                movies = os.listdir(movie_dir)
                # print(movies)
                # print(random.choice(movies))
                os.startfile(os.path.join(movie_dir,random.choice(movies)))

            elif "time" in query :
                strt = datetime.datetime.now().strftime("%H:%M;%S")
                print(strt)
                engine.setProperty('rate',190)
                speak("The time is " + strt)
                engine.setProperty('rate',230)

            elif ("quit" in query) or ("stop" in query) :   
                engine.setProperty('rate',190)
                speak("Going to Sleep...")
                engine.setProperty('rate',230)
                break
            
            elif ("search" in query) :
                query = query.replace("search"," ")
                for j in search(query, tld="co.in", num=2, stop=2, pause=2):
                    wb.open(j)
            
            elif ("validate email" in query) or ("validate the email" in query) :
                engine.setProperty('rate',190)
                speak("Enter the email to validate ")
                email = input("Enter the email to validate ")  
                speak(validate(email))
                engine.setProperty('rate',230)

            elif ("network speed" in query) or ("test speed" in query) or ("test network speed" in query) :
                engine.setProperty('rate',190)
                speak("Checking please wait...")
                speedTest()
                engine.setProperty('rate',230)

            elif ("generate strong password" in query) or ("generate password" in query) :
                engine.setProperty('rate',190)
                speak("Starting strong password generation")
                print(f"The password is {passGen()}")
                speak("Password generation complete ")
                engine.setProperty('rate',230)

            elif ("generate qrcode" in query) or ("qr" in query) :
                engine.setProperty('rate',190)
                speak("Starting QR generation")
                subprocess.run(['python','qrcodeGen.py'])
                speak("QR Generated successfully ")
                engine.setProperty('rate',230)

            elif ("download youtube video" in query) or ("download video" in query):
                engine.setProperty('rate',190)
                speak("Staring download")
                downloadVideo()
                speak("Video... Downloaded")
                engine.setProperty('rate',230)
 
        else :
            continue
        query = ""

if __name__ == "__main__":
    welcome()
    command()