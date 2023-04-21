"""
Hey Folks we had built a project of virtual assistant using python named "TECA"

    TIPS:
        *You can say your name when TECA asks "what can I call you"
        *Save or add QRcode image files to current folder to access it
        *You can play any videosong or video by using word "PLAY"
        *opening tabs can be made through keyword "OPEN" 
        *If you had the knowledge of webaddress you open certain website directly by using sentence with keyword "WEBSITE"
        * Use keyword exit in your input speech to stop or end interaction
"""
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#The code is split into different files and called them for making code simple and readable for users

#importing various packages and modules

import time                              #This module provides various time-related functions.
import datetime                          #The datetime module supplies classes for manipulating dates and times
import webbrowser as web                 #The webbrowser module provides a high-level interface to allow displaying Web-based documents to users 
import pywhatkit                         #Python offers numerous inbuilt libraries to ease our work.These are some features of pywhatkit module:Send WhatsApp messages,Play a YouTube video,Perform a Google Search,Get information on a particular topic.
import pyjokes                           #Offers you joke
import playsound
import wikipedia                         #Plays .mp3 or .avi files

#Calling different files 
from speak import teca_talk              #teca_talk funaction in speak.py is the tongue of TECA and gives a female voice to TECA
from qr import qr_acc                  #access function to access QR code from url or link
from qr import generate                  #generate function to generate QR code image
from record import teca_record           #teca_record is the ear of TECA


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#adding path of extension my default browser CHROME ,you get clear idea when you jump into code line

chrome_path="C:/Users/ANAGA.K/AppData/Local/Google/Chrome/Application/chrome.exe %s"

#Response function of TECA
def respond(text):
    if 'hello' in text:
       teca_talk("Hi, how are you?")

    elif 'your name' in text:
       teca_talk("My name is Teca. Nice to meet you.")

    elif 'time' in text:
        time=datetime.datetime.now().strftime("%I:%M %p")
        teca_talk("current time is " + time)


    elif 'today' in text:
        date=datetime.datetime.now().strftime("%d %B %Y %A")
        teca_talk("Today is " + date)


    elif 'day' in text:
        date=datetime.datetime.now().strftime("%d %B %Y %A")
        #For getting the day part only we convert date string into lists by using split()
        data=date.split()
        #data[3] represents day
        day=data[3]
        teca_talk("Today is "+ day)


    elif 'location' in text:
        teca_talk("Do you want your current location?")
        check=teca_record()     #Expecting "Yes" or "No" from user

        if 'no' in check:
            teca_talk("Which is the location you are looking upto?")
            loc=teca_record()
            url='https://www.google.com/maps/place/'+loc+'/&amp;'
            web.get().open(url)
            teca_talk("Here is the location "+loc)


        elif 'yes' in check:
            import location
            import time
            time.sleep(1)
            teca_talk("Here is your location in Googlemaps")
            web.open_new_tab("https://www.google.com/maps/")


    elif 'automate message' in text:
        from wtsp import wtsp
        wtsp()
        
    elif 'search' in text:
        teca_talk("What do you want to search?")
        info=teca_record()
        teca_talk("Here is the results for "+ info)
        pywhatkit.search(info)                      #This will perform a Google search about info


    elif 'play' in text:
        teca_talk("What do you want to play?")
        play=teca_record()
        teca_talk("playing "+ play)
        pywhatkit.playonyt(play)                    #play youtube video


    elif 'QR code' in text:
        teca_talk("What do you want? access or generate.")
        qr=str(teca_record())
        if "access" in qr :
            qr_acc()
        if 'generate' in qr:
            generate()


    elif 'meaning' in text: 
        teca_talk("Sorry,  For what want to know the meaning?")
        word=teca_record()
        pywhatkit.info(word)

    elif 'website' in text:                                     #Can use when you know webaddress
        teca_talk("Enter the link or webaddress")
        url=input("USER: ")
        teca_talk("Opening..")
        web.open_new(url)

    elif 'stack overflow' in text:
        search=input("USER: ")
        web.open_new("https://stackoverflow.com/search?q="+ search)
        
    elif 'Facebook' in text:
        teca_talk("Opening Facebook..")
        web.open_new_tab("https://www.facebook.com") 

    elif 'YouTube' in text:
        teca_talk("Opening youTube..")
        web.open_new_tab("https://www.youtube.com")

    elif 'Gmail' in text:
        teca_talk("Opening Gmail..")
        web.open_new_tab("https://mail.google.com/")  


    elif 'Discord' in text:
        teca_talk("Opening Discord..")
        web.open_new_tab("https://discord.com")  

    elif 'open' in text:
        teca_talk("Opening..")
        web.get(chrome_path).open(text)

    elif 'What is' in text:
        teca_talk("Sorry, what want to know the about")
        word=teca_record()
        teca_talk(str(wikipedia.summary(word,3)))

    elif 'Who is' in text:
        teca_talk("Sorry, what want to know the about")
        person=teca_record()
        teca_talk(str(wikipedia.summary(person,3)))
    
    elif 'joke' in text:
        teca_talk("You want me to say a joke.")
        teca_talk(pyjokes.get_joke())
        from time import sleep
        sleep(1)
        teca_talk("I hope you had fun")

    elif 'sing a song' in text:
        teca_talk("I can play default song saved in me, Stay of Justin Beiber")
        playsound.playsound("Stay.mp3")
        teca_talk("Hope you enjoyed song")

    elif 'weather' in text:
        import weather

    elif 'exit' in text:
        teca_talk("Thank you.   Hope I have helped you to do your task.Have a good day.")
        exit()
 

teca_talk("Hey,My name is Teca")

teca_talk("What can I call you?")
name=teca_record()
teca_talk("Hi,"+ name)
while(1):
    teca_talk("what can I do for u")
    text=teca_record()
    respond(text)