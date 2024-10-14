import requests
from config import weather_token

def get_weather(city, weather_token):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric"
        )
        data = r.json()

        if data.get("cod") != 200:
            return None

        cityname = data["name"]
        temp = data["main"]["temp"]
        humid = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        weather = data["weather"][0]["description"]

        return (f"Погода в {cityname}:\nТемпература: {temp} C°\n"
                f"Влажность: {humid}%\nДавление: {pressure} мм рт. ст.\n"
                f"Осадки: {weather}")
    except Exception as ex:
        return None