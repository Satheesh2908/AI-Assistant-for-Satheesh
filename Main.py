import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


# Taking voice from my System 
import pyttsx3
# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
# Get the available voices
voices = engine.getProperty('voices')
# Print the available voices
#print(voices[1].id)
# To select the Male or Female voice 
engine.setProperty('voice',voices[0].id) 
engine.setProperty('rate', 150)
# Speak Function

def speak(text):
    """
    This Function takes text and  returns voice
    Args:
        text (_type_): String
    """
    engine.say(text)
    engine.runAndWait()

# speak("Hello, This is Satheesh Kumar, Welcome to Satheesh World!!! How are you today?") 

#Speech Recognition Function

def takecommand():
    """
    This function will recognize voice input and return it as text.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query

        except sr.UnknownValueError:
            print("Sorry, I did not catch that. Please try again.")
            return "None"
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return "None"
        except Exception as e:
            print("Say that again Please...")
            return "None"
        return query
    
# This Function for wish me by using time 
def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Satheesh Sir. How are you feeling today")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon Satheesh Sir. How are you feeling today")
    
    else:
        speak("Good Evening Satheesh Sir. How are you feeling today")
    
    speak("I am Satheesh. How can I be service to you")  
    

# Test the function
# Test  Command and display the speak text
# text = takecommand()
# speak(text)

if __name__ == '__main__':
    
     wish_me()
     
     while True:
             
        query = takecommand().lower()
        print(query)
        
        if "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace('wikipedia', "")
            result = wikipedia.summary(query,sentences = 2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
            
    
        elif "youtube" in query:  
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
            
        elif "google" in query:  
            speak("Opening Google")
            webbrowser.open("google.com")
            
        elif "github" in query:  
            speak("Opening Github")
            webbrowser.open("github.com")
            
        elif 'time_date' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")   
        
        elif "goodbye" in query:
            speak("Ok Sir. I am always Happy to help you. Good Bye Catch up soon")
            exit()   
            




