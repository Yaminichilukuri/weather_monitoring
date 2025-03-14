CREATE TABLE WeatherLogs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    city VARCHAR(50),
    temperature FLOAT,
    humidity FLOAT,
    pressure FLOAT,
    weather VARCHAR(50)
);
