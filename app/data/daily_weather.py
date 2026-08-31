import pandas as pd

def daily_data(response):
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

    return daily_data