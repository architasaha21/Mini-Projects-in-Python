import requests
import json
import os

city = input("Enter the city name : ")

url = f"https://api.weatherapi.com/v1/current.json?key=74f26d3448a24edea91154754250601&q={city}"

r = requests.get(url)

# print(r.text,type(r.text))

wdic = json.loads(r.text)

w = wdic["current"]["temp_c"]


print(f"The temperature in {city} is {w} degree celsius")
