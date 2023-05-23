# Making the WeatherApp using Python
import requests
import json
import os

city = input("Enter the name of the city: ")
url = f"http://api.weatherapi.com/v1/current.json?key=c87e6795fa08498ea23183552232305&q={city}"

r = requests.get(url)
# print(r.text)
# We will see that
# print(type(r.text))
# To convert the string into dictionary we will use json format
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])