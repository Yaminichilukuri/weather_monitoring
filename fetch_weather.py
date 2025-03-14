import requests
import pandas as pd
import datetime

# OpenWeatherMap API Key (Replace with your actual key)
API_KEY = "c1397ee0ab43f16c097244cb08358d0d"

# City Name (Make sure it's in quotes)
CITY = "Hyderabad"

# API URL
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Fetch Data from API
response = requests.get(URL)
data = response.json()

# Extract Required Fields
weather_data = {
    "Timestamp": [datetime.datetime.now()],
    "City": [CITY],
    "Temperature (°C)": [data["main"]["temp"]],
    "Humidity (%)": [data["main"]["humidity"]],
    "Pressure (hPa)": [data["main"]["pressure"]],
    "Weather": [data["weather"][0]["description"]]
}

# Convert to DataFrame
df = pd.DataFrame(weather_data)

# Save to CSV (Append Mode)
df.to_csv("weather_data.csv", mode="a", index=False, header=False)

print("New weather data saved to weather_data.csv!")
print(df)
