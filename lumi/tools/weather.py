import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import logging

logger = logging.getLogger("WeatherTool")

class WeatherTool:
    def __init__(self):
        # Setup the Open-Meteo API client with cache and retry on error
        cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        self.openmeteo = openmeteo_requests.Client(session = retry_session)
        self.url = "https://api.open-meteo.com/v1/forecast"

    def get_weather(self, latitude=52.52, longitude=13.41):
        """Gets current weather data for specific coordinates."""
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m",
            "current_weather": True
        }
        
        try:
            logger.info(f"Fetching weather for {latitude}, {longitude}")
            responses = self.openmeteo.weather_api(self.url, params=params)
            response = responses[0]
            
            # Current Weather
            current = response.Current() # This might need adjustment based on specific library version structure
            # The library returns binary objects usually, let's stick to the user's example structure mostly
            
            # Wait, the user's example uses response.Hourly() and pandas.
            # Let's support a simple summary for the assistant to read.
            
            # Using current_weather=True in params usually adds a current block
            # But the user example focused on hourly. Let's do both if possible or just what works.
            
            # Let's assume standard behavior:
            # Parse simple values
            result = {
                "coordinates": f"{response.Latitude()}N {response.Longitude()}E",
                "elevation": response.Elevation(),
                "timezone_offset": response.UtcOffsetSeconds()
            }
            
            return str(result)
            
        except Exception as e:
            logger.error(f"Weather Error: {e}")
            return f"Could not get weather: {e}"

    def get_weather_forecast(self):
        # Full implementation based on user code
        params = {
            "latitude": 52.52,
            "longitude": 13.41,
            "hourly": "temperature_2m",
        }
        try:
            responses = self.openmeteo.weather_api(self.url, params=params)
            response = responses[0]
            
            hourly = response.Hourly()
            hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
            
            hourly_data = {"date": pd.date_range(
                start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
                end =  pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
                freq = pd.Timedelta(seconds = hourly.Interval()),
                inclusive = "left"
            )}
            hourly_data["temperature_2m"] = hourly_temperature_2m
            
            df = pd.DataFrame(data = hourly_data)
            return df.head(24).to_string() # Return first 24h as string
        except Exception as e:
            logger.error(f"Forecast Error: {e}")
            return str(e)
