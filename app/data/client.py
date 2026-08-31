import openmeteo_requests

def client(sessao):
    openmeteo = openmeteo_requests.Client(session = sessao)
    
    return openmeteo