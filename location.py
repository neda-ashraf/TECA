#FOR LOCATION INFORMATION



import requests                                 # Python Requests is a powerful tool that provides the simple elegance of Python to make HTTP requests to any API in the world.
from speak import teca_talk                     #Tongue of TECA


res=requests.get("https://ipinfo.io/")          #get requests is used to to obtain the requested data from the specific server
data=res.json()                                 #json() The json() method of the Request interface reads the request body and returns it as a promise that resolves with the result of parsing the body text as JSON 

city=data['city']
region=data['region']
ip_address=['ip']

location=data['loc'].split(',')                 
latitude=location[0]
longitude=location[1]

teca_talk('your city is ' + city+ ' ,your latitude is '+ latitude+ ' and your longitude is ' + longitude)