import pyttsx3
import win32com.client as wincom

if __name__ == '__main__':
    print("Welcome to Robo Speaker 1.1. Created by Archita")
    x=input("Enter the text you want to convert to speech (or 'q' to quit): ")
    
    # If the user enters 'q', the program will quit
    engine = pyttsx3.init()
    
    while True:
        x = input("Enter the text you want to convert to speech (or 'q' to quit): ")
        
        if x.lower() == 'q':
            print("Quitting Robo Speaker....")
            break
        
        speak=wincom.Dispatch("SAPI.SpVoice")
        speak.Speak(x)
        # engine.say(x)  # Convert text to speech
        # engine.runAndWait()
    