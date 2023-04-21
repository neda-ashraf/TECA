import pyttsx3                          #pyttsx3 is a text-to-speech conversion library in Python
import speech_recognition as sr         #recognizes voice of user


def teca_record():
    
    speech=pyttsx3.init()
    speech.setProperty("rate",200)
    voices=speech.getProperty('voices')
    speech.setProperty('voice',voices[1].id)

    a=sr.Recognizer()

    with sr.Microphone() as source:
        a.adjust_for_ambient_noise(source)
        voice=a.listen(source)
        
        text=''
        try:
            text=a.recognize_google(voice)
            print("USER: " + text)


        except sr.UnknownValueError:
            speech.say("Sorry I don't get that")
            speech.runAndWait()
            print("TECA: Sorry I don't get that........")

        except sr.RequestError:
            speech.say("Sorry my speech server is down")
            speech.runAndWait()
            print("TECA: Sorry my speech server is down.....")
        return text
