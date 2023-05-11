import requests
import datetime


def get_img(weather: str) -> str:
    weather_path = 'assets/default.jpg'
    if weather == 'Thunderstorm':
        weather_path = 'assets/thunderstorm.jpg'
    if weather == 'Drizzle':
        weather_path = 'assets/dizzle.jpg'
    if weather == 'Rain':
        weather_path = 'assets/rain.jpg'
    if weather == 'Snow':
        weather_path = 'assets/snow.jpg'
    if weather == 'Mist':
        weather_path = 'assets/mist.jpg'
    if weather == 'Smoke':
        weather_path = 'assets/smoke.jpg'
    if weather == 'Haze':
        weather_path = 'assets/haze.jpg'
    if weather == 'Dust':
        weather_path = 'assets/dust.jpg'
    if weather == 'Fog':
        weather_path = 'assets/fog.jpg'
    if weather == 'Sand':
        weather_path = 'assets/sand.jpg'
    if weather == 'Clouds':
        weather_path = 'assets/clouds.jpg'
    if weather == 'Clear':
        weather_path = 'assets/clear.jpg'
    return weather_path


def get_weather_data(city_name: str) -> str:
    api_key = #put your api key here in str ofc
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city_name, api_key)
    json = (requests.get(url)).json()
    mausam = (((json["weather"])[0])["main"])
    desc = (((json["weather"])[0])["description"])
    tapman = int((json['main']['temp']) - 273)
    date = datetime.date.today()
    time = (datetime.datetime.now()).time()
    hr = time.hour
    min1 = time.minute
    sec = time.second
    time = (f'{hr}:{min1}:{sec}')
    return [mausam, (f'''
City - {city_name}\n
Weather - {(desc)}\n
Temperature - {tapman} degree celcius\n
Date - {date}\n
Time - {time}
''')]

