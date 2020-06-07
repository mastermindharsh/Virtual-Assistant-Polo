import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# female voice 
# print(voices[1].id)

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour =  int(datetime.datetime.now().hour)
    if hour>=6 and hour<=12:
        speak("Good morning mastermind")
    elif hour>12 and hour<=17:
        speak("Good afternoon mastermind")
    elif hour>17 and hour<=23:
        speak("Good evening mastermind!")
    else: 
        speak("It's late sir, you should sleep now. Good night mastermind!")
    if hour>=6 and hour<=23:
        speak("I am polo Sir! Please tell me how may I help you? ")

def takeCommand():
    # Microphone input to speech output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print('Recognising...')
        querry = r.recognize_google(audio, language='en-in')
        print(f'User said: {querry}\n')
    
    except Exception as e:
        # print(e)
        print('Say that again please...')
        return "None"
    return querry

if __name__ == "__main__":
    wishMe()