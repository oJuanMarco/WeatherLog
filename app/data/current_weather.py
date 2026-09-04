# chamada da parte de clima atual da API e printa para o usuário ao consultar
def current_data(response):
    try:
        current = response.Current()

        current_temperature_2m = current.Variables(0).Value()
        current_temperature_2m = str(current_temperature_2m)[:4]
        current_temperature_2m = float(current_temperature_2m)

        current_apparent_temperature = current.Variables(1).Value()
        current_apparent_temperature = str(current_apparent_temperature)[:4]
        current_apparent_temperature = float(current_apparent_temperature)


        print(f"Temperatura atual: {current_temperature_2m} ºC \nSensação térmica: {current_apparent_temperature} ºC ")
    
    except httpx.TimeoutException:
        print("A API demorou muito para responder (Timeout).")
    except httpx.ConnectError:
        print("Não foi possível conectar ao servidor. Verifique a internet.")
    except httpx.HTTPStatusError as e:
        print(f"A API retornou um erro HTTP: {e.response.status_code}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado em current_data: {e}")