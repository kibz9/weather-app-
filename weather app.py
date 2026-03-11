import datetime as dt
import requests

Base_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "be3d7ffb219ef3e5cd093beb966b1339"
CITY = "kenya"

def  kelvin_to_celsius_fahrenhit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
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
