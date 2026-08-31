def current_data(response):
    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()
    current_apparent_temperature = current.Variables(1).Value()

    print(f"Temperatura atual: {current_temperature_2m} \nSensação térmica: {current_apparent_temperature} ")