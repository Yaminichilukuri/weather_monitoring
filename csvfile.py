# Save to CSV (Append Mode)
df.to_csv("weather_data.csv", mode="a", index=False, header=False)

print("New weather data saved to weather_data.csv!")
