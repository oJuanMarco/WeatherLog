from config import config

def params(openmeteo):
    url = config()

    params = {
        "latitude": 52.52,
        "longitude": 13.41,
        "daily": ["temperature_2m_max", "temperature_2m_min", "precipitation_probability_max", "apparent_temperature_mean", "temperature_2m_mean", "rain_sum"],
        "current": ["temperature_2m", "apparent_temperature"],
        "timezone": "America/Sao_Paulo",
    }

    responses = openmeteo.weather_api(url, params = params)

    return responses