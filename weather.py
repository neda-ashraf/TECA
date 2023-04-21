# importing requests and json
import requests, json
from speak import teca_talk

res = requests.get("https://ipinfo.io/") #get requests is used to to obtain the requested data from the specific server
data = res.json()

# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
city = data['city']
API_KEY = "a1e6626aaa9a4ba31d8cf6244c6b65af"
# upadting the URL
URL = BASE_URL + "q=" + city + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)

# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
   # getting temperature
   temperature = main['temp']
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   # weather report
   report = data['weather']
   teca_talk(f"city: {city}")
   teca_talk(f"Temperature: {temperature}")
   teca_talk(f"Humidity: {humidity}")
   teca_talk(f"Pressure: {pressure}")
   teca_talk(f"Weather Report: {report[0]['description']}")
  
else:
   # showing the error message
   print("Error in the HTTP request")