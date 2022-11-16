from weatherData import get_coordinates, get_weather

def weather():
    data = get_weather(get_coordinates())
    return f'{data.location}, {data.description}\nTemperature is {data.temperature}°C, feels like {data.temperature_feeling}°C'

def wind():
    data = get_weather(get_coordinates())
    return f'{data.wind_direction} wind {data.wind_speed} m/s'

def sun_time():
    data = get_weather(get_coordinates())
    return f'Sunrise: {data.sunrise.strftime("%H:%M")}\nSunset: {data.sunset.strftime("%H:%M")}'