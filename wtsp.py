
from speak import teca_talk
import pywhatkit

def wtsp():
   
    teca_talk(" Input the number of reciever")
    num=input("USER: ")                             
    teca_talk("Enter the message to send to " + num)
    msg=input("USER: ")                            
    teca_talk("In hour and minutes:")       
    hr=int(input("USER: "))                      
    min=int(input("USER: "))
    teca_talk("Automating message")                 
    pywhatkit.sendwhatmsg( ("+91"+num),msg,hr,min)                                                                                                    
                                               