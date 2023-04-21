
from speak import teca_talk
import qrcode
import pyttsx3
import cv2
from pyzbar.pyzbar import decode
import webbrowser as web
import random

def generate():
    teca_talk("Input the link to generate qr code")
    a=input("USER: ")
    #making the link to qr code
    img=qrcode.make(a)
    r=random.randint(1,1000000)
    a_file="QR-"+str(r)+".jpg"
    #saving the image of qr code to a file
    img.save(a_file)
    teca_talk("your QR code is being saved as "+ a_file)
    
def qr_acc():
    im=cv2.QRCodeDetector()
    teca_talk("Enter the file name.jpg ")
    pic=input("USER: ")
    find,points,straight_qrcode=im.detectAndDecode(cv2.imread(pic))
    teca_talk("Decoding your QR code image,I can say it as:"  + find)
    web.open_new_tab(find)
