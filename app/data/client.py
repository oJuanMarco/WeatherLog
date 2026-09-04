import openmeteo_requests

def client(sessao):
    try:
        openmeteo = openmeteo_requests.Client(session = sessao)
        return openmeteo
    
    except httpx.TimeoutException:
        print("A API demorou muito para responder (Timeout).")
    except httpx.ConnectError:
        print("Não foi possível conectar ao servidor. Verifique a internet.")
    except httpx.HTTPStatusError as e:
        print(f"A API retornou um erro HTTP: {e.response.status_code}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado em client: {e}")