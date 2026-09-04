import pandas as pd
from app.data.response import params
from app.data.client import client
from app.data.setup import session
from app.data.current_weather import current_data
from app.data.daily_weather import daily_data
import asyncio


async def init():
    try:
        await asyncio.sleep(3)
        start = session()
        openmeteo = client(start)
        semiresponse = params(openmeteo)

        response = semiresponse[0]
        print(f"Local: {response.Timezone()}")

        # Process current data. The order of variables needs to be the same as requested.
        current_data(response)
        # Process daily data. The order of variables needs to be the same as requested.
        daily_dataframe = pd.DataFrame(data = daily_data(response))

        return daily_dataframe

    except httpx.TimeoutException:
        print("A API demorou muito para responder (Timeout).")
    except httpx.ConnectError:
        print("Não foi possível conectar ao servidor. Verifique a internet.")
    except httpx.HTTPStatusError as e:
        print(f"A API retornou um erro HTTP: {e.response.status_code}")
    except FileNotFoundError as e:
        print(f'Operação de criar dataframe em falha por não encontrar o arquivo: {e}')
    except asyncio.TimeoutError as e:
        print(f'Limite de tempo atingido para execução: {e}')
    except asyncio.CancelledError as e:
        print(f'Task cancelada antes da execução: {e}')
    except asyncio.InvalidStateError as e:
        print(f'Operação inválida no estado de execução: {e}')
    except Exception as e:
        print(f"Ocorreu um erro inesperado em init: {e}")