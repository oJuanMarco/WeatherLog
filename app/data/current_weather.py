def current_data(response):
    current = response.Current()

    current_temperature_2m = current.Variables(0).Value()
    current_temperature_2m = str(current_temperature_2m)[:4]
    current_temperature_2m = float(current_temperature_2m)

    current_apparent_temperature = current.Variables(1).Value()
    current_apparent_temperature = str(current_apparent_temperature)[:4]
    current_apparent_temperature = float(current_apparent_temperature)


    print(f"Temperatura atual: {current_temperature_2m} ºC \nSensação térmica: {current_apparent_temperature} ºC ")