import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognizer as sr #pip install speechRecognizer
import wikipedia  #pip install wikipedia
import webbrowser
import os
import smtplib 

engine = pyttsx3.init('sapi5')
#microsoft ka voice- speech api
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    '''Mainn function for speech audio'''
    
def wishMe():
    '''wishes according to time of day'''
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <=12:
        speak("Good Morning!!")
    elif hour >12 and hour <18:
        speak("Good Afternoon!")
    else:
        speak("good evening!")
    speak("I'm divi your desktop assistant. How can i help you?")  

def takeCommand():
    #it takes microphone input from the user and returns string o/p
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language="en-in")
        #uses google voice-text engine
        print("user said:", query,"\n")
    except Exception as e:
        print("Say that again please..")
        return "None"
    return query

def sendEmail(to,cont):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'pswd')
    server.sendmail('youremail@gmail.com',to, cont)
    server.close()
    
if __name__ == "__main__":
       # speak("divi is here")
       #to execute various commands
        wishMe()
        while True:
            query = takeCommand().lower()
            
            if 'wikipedia' in query:
                speak('Searching wikipedia..')
                query = query.replace("wikipedia","")
                res = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(res)
                speak(res)
            
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                
            elif 'open google' in query:
                webbrowser.open("google.com")
                
            elif 'open spotify' in query:
                webbrowser.open("spotify.com")
            
            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
            
            elif 'play music' in query:
              #music_dir = give path 
              songs = os.listdir(music_dir)
              print(songs)
              os.startfile(os.path.join(music_dir, songs[0]))
            
            elif 'time' in query:
             steTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"The time is {steTime}")
             
            elif 'open code' in query:
                #codePath = give path
                os.startfile(codePath)
            
            elif 'email to divya' in query:
                try:
                    speak("What should  i say?")
                    cont = takeCommand()
                    to = "youremail@gmail.com"
                    sendEmail(to,cont)
                    speak("Email has been sent")
                except Exception as e:
                    speak("Email not sent loser")
                    
           #can add more features like opening browsers, gallery, downloads, etc                    
          
