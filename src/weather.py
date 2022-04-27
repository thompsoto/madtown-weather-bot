import datetime as dt
import requests

def kelvin_to_fahrenheit(kelvin):
    return int(round((kelvin - 273.15) * (9/5) + 32, 0))

weather_key = open('weatherkey.txt', 'r').read()
url = "https://api.openweathermap.org/data/2.5/weather?q=Madison,wi,us&appid=" + weather_key
data = requests.get(url).json()

# Extracting data fields below
curr_time = int(str(dt.datetime.now())[11:13])
curr_temp = kelvin_to_fahrenheit(data['main']['temp'])
feels_like = kelvin_to_fahrenheit(data['main']['feels_like'])
description = data['weather'][0]['description'].lower().capitalize()
wind_speed = round(data['wind']['speed'] * 2.23694, 1)
sunrise = str(dt.datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone']))[12:16]
temp_sunset = str(dt.datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone']))[11:16]
sunset = str(int(temp_sunset[:2]) % 12) + temp_sunset[2:]
morning_msg = f"Good morning.\nIt is currently {str(curr_temp)}\N{DEGREE SIGN}F, feels like {str(feels_like)}\N{DEGREE SIGN}F.\n{description}. Wind Speed: {str(wind_speed)} mph.\nExpect the sun to set today at {sunset}pm.\nHave a great day."
night_msg = f"Good afternoon.\nIt is currently {str(curr_temp)}\N{DEGREE SIGN}F, feels like {str(feels_like)}\N{DEGREE SIGN}F.\n{description}. Wind Speed: {str(wind_speed)} mph.\nExpect sunrise tomorrow at {sunrise}am.\nHave a great night."