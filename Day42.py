import requests
from datetime import datetime

API_KEY = "YOUR_API_KEY"

print("===== WEATHER APP =====")

city = input("Enter City Name: ")

url = (
    f"https://api.openweathermap.org/data/2.5/weather?"
    f"q={city}&appid={API_KEY}&units=metric"
)

try:
    response = requests.get(url)
    data = response.json()

    if data["cod"] != 200:
        print("❌ City Not Found!")
        exit()

    city_name = data["name"]
    country = data["sys"]["country"]

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    weather = data["weather"][0]["description"].title()

    wind_speed = data["wind"]["speed"]

    report = f"""
========== WEATHER REPORT ==========

Date & Time : {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

Location    : {city_name}, {country}

Temperature : {temperature} °C
Feels Like  : {feels_like} °C

Humidity    : {humidity} %
Pressure    : {pressure} hPa

Wind Speed  : {wind_speed} m/s

Condition   : {weather}

====================================
"""

    print(report)

    with open("weather_history.txt", "a") as file:
        file.write(report)
        file.write("\n")

    print("✅ Weather History Saved!")

except Exception as e:
    print("❌ Error:", e)
