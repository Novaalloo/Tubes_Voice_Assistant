import pyttsx3
import speech_recognition as sr 
import os
import re
import webbrowser
import datetime
import wikipedia

print("initializing Jarvis")

MASTER = "Naufal"

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

#speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# function
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
        speak("")


#microphone 
def myCommand():
    "listen commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language="en-us")
        print("You : " + command + "\n")

    except Exception as e:
        print("Say that again please")
        command = myCommand();

    return command


# main start
speak("Hello my name is Jarvis, i can help you !!")
wishMe()
command = "myCommand()"


def assistant(command):
    "if statemenet for executing commands"

    if "hello" in command:
        print("Jarvis : Hello Naufal, how can I help you ?")
        speak("Hello Naufal, how can I help you ?")

    elif "open Google" in command:
        reg_ex = re.search("google (.*)", command)
        url = "https://www.google.com/"
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + "r/" + subreddit
        webbrowser.open(url)
        print("Done")
        speak("Open Google have done")

    elif "open YouTube" in command:
        reg_ex = re.search("web (.*)", command)
        url = "https://www.youtube.com/"
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + "r/" + subreddit
        webbrowser.open(url)
        print("Done")
        speak("Open YouTube have done")

    elif "what time" in command:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print("Time " + strTime)
        speak("The time is " + strTime)

    elif "Wikipedia" in command:
        speak("searching Wikipedia")
        command = command.replace("Wikipedia", "")
        results = wikipedia.summary(command, sentences=3)
        print(results)
        speak(results)

    elif "open website" in command:
        reg_ex = re.search("open website (.+)", command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = "https://www." + domain
            webbrowser.open(url)
            print("Done")
            speak("Open Website have done")
        else:
            pass

    elif "thank you" in command:
        print("Jaris : Your welcome Naufal, happy to help you, have a good day !!")
        speak("Your welcome Naufal, happy to help you, have a good day !!")
        exit()

while True:
    assistant(myCommand())

