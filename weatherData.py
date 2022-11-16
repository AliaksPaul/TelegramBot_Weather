from dataclasses import dataclass
from enum import IntEnum
from datetime import datetime
import requests
import json


key = "48abaa83c10e6e6fe1d4d4a99e44ed27"
K = 273.15

@dataclass(frozen=True)
class Coordinates:
    latitude: float
    longitude: float 


@dataclass(frozen=True)
class Weather:
    location: str
    temperature: float
    temperature_feeling: float
    description: str
    wind_speed: float
    wind_direction: str
    sunrise: datetime
    sunset: datetime


class WindDirection(IntEnum):
    North = 0
    NorthEast = 45
    East = 90
    SothEast= 135
    South = 180
    SouthWest= 225
    West = 270
    NorthWest= 315


def get_ip_data():
    url = 'https://ipinfo.io/json/'
    data = requests.get(url)
    data = json.loads(data.text)
    return data

def get_weather(coordinates):
    data = get_weather_response(coordinates.latitude, coordinates.longitude)
    weather = parse_weather_response(data)
    return weather


def get_coordinates():
    data = get_ip_data()
    latitude = data['loc'].split(',')[0]
    longitude = data['loc'].split(',')[1]

    return Coordinates(latitude, longitude)

def get_weather_response(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"
    data = requests.get(url)
    data = json.loads(data.text)
    return data

def parse_weather_response(weather_response):
    data = weather_response
    return Weather(
        location = parse_location(data),
        temperature = parse_temperature(data),
        temperature_feeling = parse_temperature_feeling(data),
        description = parse_description(data),
        wind_speed = parse_wind_speed(data),
        wind_direction = parse_description(data),
        sunrise = parse_sun_time(data, 'sunrise'),
        sunset =  parse_sun_time(data, 'sunset')
    )

def parse_location(dict):
    return dict['name']

def parse_temperature(dict):
    return round(float(dict['main']['temp']) - K, 2)

def parse_temperature_feeling(dict):
    return round(float(dict['main']['feels_like']) - K, 2)

def parse_description(dict):
    return dict['weather'][0]['description'].capitalize()

def parse_sun_time(dict, time):
    return datetime.fromtimestamp(dict['sys'][time])

def parse_wind_speed(dict):
    return dict['wind']['speed']
     
def parse_wind_direction(dict):
    degrees = round((dict['wind']['deg'])/45)*45 
    if degrees == 360: degrees == 0
    return WindDirection(degrees).name
