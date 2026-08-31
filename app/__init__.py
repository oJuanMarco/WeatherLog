import pandas as pd
from app.data.response import params
from app.data.client import client
from app.data.setup import session
from app.data.current_weather import current_data
from app.data.daily_weather import daily_data


def init():
    start = session()
    openmeteo = client(start)
    semiresponse = params(openmeteo)

    response = semiresponse[0]
    print(f"Local: {response.Timezone()}")

    # Process current data. The order of variables needs to be the same as requested.
    current_data(response)
    # Process daily data. The order of variables needs to be the same as requested.
    daily_dataframe = pd.DataFrame(data = daily_data(response))


    print("\nDados da semana\n", daily_dataframe)