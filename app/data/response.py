from config import config
# define parametroes à serem solicitados à API e sua ordem em cime da url do config
def params(openmeteo):
    try:
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

    except httpx.TimeoutException:
        print("A API demorou muito para responder (Timeout).")
    except httpx.ConnectError:
        print("Não foi possível conectar ao servidor. Verifique a internet.")
    except httpx.HTTPStatusError as e:
        print(f"A API retornou um erro HTTP: {e.response.status_code}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado em response: {e}")