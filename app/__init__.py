import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

def init():
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 52.52,
        "longitude": 13.41,
        "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_probability_max", "apparent_temperature_mean", "temperature_2m_mean", "rain_sum"],
        "current": ["temperature_2m", "apparent_temperature"],
        "timezone": "America/Sao_Paulo",
    }
    responses = openmeteo.weather_api(url, params = params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    print(f"Local: {response.Timezone()}")

    # Process current data. The order of variables needs to be the same as requested.
    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()
    current_apparent_temperature = current.Variables(1).Value()

    print(f"Temperatura atual: {current_temperature_2m} \nSensação térmica: {current_apparent_temperature} ")

    # Process daily data. The order of variables needs to be the same as requested.
    daily = response.Daily()
    daily_temperature_2m_mean = daily.Variables(4).ValuesAsNumpy()
    daily_apparent_temperature_mean = daily.Variables(3).ValuesAsNumpy()
    daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
    daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
    daily_precipitation_probability_max = daily.Variables(2).ValuesAsNumpy()
    daily_rain_sum = daily.Variables(5).ValuesAsNumpy()

    daily_data = {
        "data": pd.date_range(
            start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
            end =  pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = daily.Interval()),
            inclusive = "left"
        ).tz_convert(response.Timezone().decode())
    }

    daily_data["temperatura_media"] = daily_temperature_2m_mean
    daily_data["sensacao_termica_media"] = daily_apparent_temperature_mean
    daily_data["maxima"] = daily_temperature_2m_max
    daily_data["minima"] = daily_temperature_2m_min
    daily_data["chances_de_chuva"] = daily_precipitation_probability_max
    daily_data["volume_de_chuva(mm)"] = daily_rain_sum

    daily_dataframe = pd.DataFrame(data = daily_data)
    print("\nDados da semana\n", daily_dataframe)