import pyttsx3 as py
speech=py.init() 
                                           

def teca_talk(text):
    voices=speech.getProperty('voices')
    speech.setProperty('voice',voices[1].id)
    speech.setProperty("rate",160)
    speech.setProperty('volume',1)
    print("TECA: " + text)
    speech.say(text)
    speech.runAndWait()

