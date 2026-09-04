import requests_cache
from retry_requests import retry

def session():
     try:
          # Setup the Open-Meteo API client with cache and retry on error
          cache_session = requests_cache.CachedSession('week_weather_data', expire_after = 3600)
          retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)

          return retry_session

     except httpx.TimeoutException:
        print("A API demorou muito para responder (Timeout).")
     except httpx.ConnectError:
        print("Não foi possível conectar ao servidor. Verifique a internet.")
     except httpx.HTTPStatusError as e:
        print(f"A API retornou um erro HTTP: {e.response.status_code}")
     except Exception as e:
        print(f"Ocorreu um erro inesperado em Setup: {e}")