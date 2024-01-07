### What is Jarvis AI Assistant?

JARVIS is a python program which is aimed at automating and implementing various routines in the software. This can then be scheduled to run always on the system device. The AI will then be active always to accept user tasks. This AI can perform various routines like search on internet and provide the results on the browser, encrypt, decrypt and merge pdf files, download any video from youtube offline, generate password for you, test the network speed you are connected with and even shutdown, restart or lock the device for you.

### Overview
JARVIS was developed in python programming language including various standard libraries and packages like os, shutil, datetime etc, and various external libraries and packages like pyttsx3, PyPDF2, qrcode, wikipedia, speech-recognition etc. 

### Get Started
Make sure you must have installed python interpreter. If not, you can install from the website : *[Python|downloads](https://www.python.org/downloads/)*.

a. Clone the repository into your system via any of the two following bash command  
```
git clone git@github.com:anvitgupta01/Jarvis-AI-Assistant.git
```

```
git clone https://github.com/anvitgupta01/Jarvis-AI-Assistant.git
```

The above command will simply clone the whole repository into your system and create a folder in your present working directory with all the source files of Jarvis Windows Assistant.

b. Upgrade the pip packages installed before installing new packages via the following command :
```
python.exe -m pip install --upgrade pip
```

c. After upgrading the installed packages, its time to install the packages required to run the JARVIS on your system. Install required packages with the below command.
```
pip install -r requirements.txt
```

d. Now you have installed all the external packages required to run the program, you can easily run the program by calling python interpreter for [*Assistant.py*](https://github.com/anvitgupta01/Jarvis-AI-Assistant/blob/master/Assistant.py) by the below command.
```
python Assistant.py
```

It starts by Greeting you with Good Morning, Afternoon or Evening according to the daytime. Start asking for some internet results, network speed, work with files, generate a strong password etc.


### Developing JARVIS : Moving through the source code

a. The source code starts with *["Assistant.py"](https://github.com/anvitgupta01/Jarvis-AI-Assistant/blob/master/Assistant.py)* which contains actual implemenation logic for the software. Different main sections of the program are highighted below with some explanation on how to use and what has been done.

```
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
from WorkWithPDF import merge,decrypt,encrypt
```
The above code includes all the standard and external libraries and packages as well as user defined source files required to bring the functionality to the Jarvis. 
The important highlight for the libraries are given below :

1. Standard built-in Modules - These are those modules which came with python interpreter and present in python standard library. These can be used direclty without installing once you import them. JARVIS includes the below standard modules :
   
- datetime - A standard module in python used to work with date and time.
- os - One of the most important module of python standard library deals with interacting and performing the tasks which can only be performed by the OS of the system. 'os' module will indirectly interact with the OS.
- webbrowser - To open any application using a browser, we need a python module called 'webbrowser'. This is present in python standard library and not need to explicitly installed.
- random - To generate any random number, python uses functions or routines present in 'random' module. This is a standard library module.
- subprocess - A python standard library module used to run other application files from the main python files. With the help of this module, python somewhat implements **separation of concern**.

2. External Modules - Modules that are not part of python standard library must have to installed manually by using 'pip' which is the package manager of python.
     ```
     pip install <___Module_name___>
     ```
   JARVIS uses the following external modules :
 - pyttsx3 - The module used to implement text to speech conversion in python
 - speech_recognition - The module used to recognise the speech of the user. This module will also use the microphone of our system. To use the microphone, python uses another module called 'pyaudio', which also has to be installed manually with the above written command. With PyAudio, you can easily use Python to play and record audio on a variety of platforms, such as GNU/Linux, Microsoft Windows, and Apple macOS.
 - wikipedia - To get results from wikipedia, 'wikipedia' need to be installed in the python.

3. User-defined python files - These are also python program files which are used to implement more functionality to the Jarvis. These will be discussed later on.


```
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
```

The above program segment does intialization of various resources required in other sections of the program. 
- This segment starts with getting connected with 'googlesearch', so that Jarvis is able to search on Google whenever user wants. If any error occurs, then it will print the message error concerned message. To connect with googlesearch, you need to install another python module called 'google' with the command ```pip install google```.
- The next subsegment is trying to locate the chrome web browser to use it as the deafult for this program.
- Setting up the engine, so that our python program can speak and interact with us.
    - Different types of voices are present in the system. You can use any of them to be used by the program.
    - 'rate' defines the speed of speaking by the program. It can be changed at any time in the program. The default value has been set to 230.
- Recogniser and Microphone are enabled to allow human to communicate with JARVIS.


  ```
  if __name__ == "__main__":
    welcome()
    command()
  ```
The main function calls two functions :
      - welcome - Greets the user when the program has been started.
      - command - This has the actual implementation logic of the Jarvis. By running this function, Jarvis is now able to take commands from the user and then process it accordingly.

```
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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
            speak("Please speak again")
            engine.setProperty('rate',230)
            return ""
        return query
```




**Note that this AI will not provide the complete automation of the device and always some manual intervention will be required for giving required input to the AI like any website link, file path, passwords etc, also scheduling have to be done in advance for running it at different times. You can edit it according to your requirements, add more functions, remove which are not required.** 

Feel free to contact me at the above specified email address for any support and any inconsistency in the JARVIS Windows Assistant.
