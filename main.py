import requests
import datetime

def fetch_weather():
    city = "Mumbai"  # You can change the city here
    api_key = "761a9c10e8bada6cbe53c351dd72699a"  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        
        # Print the weather data for debugging
        print("Weather Data:", weather_data)
        
        # Write the weather data to a log file
        try:
            with open("weather_log.txt", "a") as file:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{timestamp} - Weather Data: {weather_data}\n")
            print("Weather data logged successfully.")
        except Exception as e:
            print(f"Error logging weather data: {e}")
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    fetch_weather()
