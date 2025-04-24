import requests
from datetime import datetime

def fetch_weather():
    city = "Mumbai"  # You can change the city here
    api_key = "84a8b174f93ebcb6dc7e7e058be23087"  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        log = f"{datetime.now()}: {city} - {weather}, {temp}°C\n"
    else:
        log = f"{datetime.now()}: Failed to fetch data - {data.get('message', 'Unknown error')}\n"

    with open("weather_log.txt", "a") as f:
        f.write(log)

if __name__ == "__main__":
    fetch_weather()
