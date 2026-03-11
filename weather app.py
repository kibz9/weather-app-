import datetime as dt
import requests # use pip install request or pip3 install request
#if both command dont work in the  terminal install pip use this command
# python -m ensurepip --upgrade  after typing this command type
#python -m pip install  request 
#then test  by running your  program again

Base_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "your _api_key_here"# create an account using  open weather  app after creating click account then api key  then you will see an api key
CITY = "kenya" # enter a  any city after generating  an api king

def  kelvin_to_celsius_fahrenhit(kelvin): # use both degrees or fahrenhit depending  on your  location
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 3
    return celsius, fahrenheit

url = Base_URL + "?appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()
temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenhit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenhit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f" Temperature in {CITY}: {temp_celsius:.2f}°C ({temp_fahrenheit:.2f}°F)")
print(f" Feels like in {CITY}: {feels_like_celsius:.2f}°C ({feels_like_fahrenheit:.2f}°F)")
print(f" Wind Speed in {CITY}: {wind_speed * 3.6:.2f} km/h")  # Convert m/s to km/h
print(f" Humidity in {CITY}: {humidity}%")
print(f" Description in {CITY}: {description}")
print(f"general weather in {CITY}: {description}")
print(f" Sunrise in {CITY}: {sunrise_time} local time")
print(f" Sunset in {CITY}: {sunset_time} local time")

print(response)



