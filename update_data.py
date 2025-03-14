from sqlalchemy import create_engine

# Database Connection (Modify for your setup)
engine = create_engine("sqlite:///weather.db")  # For SQLite
# engine = create_engine("postgresql://username:password@localhost:5432/weather_db")  # For PostgreSQL

# Store Data in SQL
df.to_sql("WeatherLogs", engine, if_exists="append", index=False)

print("Data stored in SQL database!")
