import pandas as pd
from app.functions.init import init
import asyncio
# função de tratamento de dados recebidos da API para futuro export e permanência
async def treat(db):
    try:
        db = await db

        for column in db.columns:
            if db[column].dtype == "datetime64[s, America/Sao_Paulo]":
                db[column] = db[column].astype(str).str.replace("-","/").apply(lambda x: x[:10])
            else:
                db[column] = db[column].astype(str).apply(lambda x: x[:4])
                db[column] = db[column].astype(float)

        print(db)
        return db

    except asyncio.TimeoutError as e:
        print(f'Limite de tempo atingido para execução: {e}')
    except asyncio.CancelledError as e:
        print(f'Task cancelada antes da execução: {e}')
    except asyncio.InvalidStateError as e:
        print(f'Operação inválida no estado de execução: {e}')
    except FileNotFoundError as e:
        print(f'Operação de tratamento em falha por não encontrar o arquivo: {e}')
    except Exception as e:
        print(f'Ocorreu um erro inesperado em treat: {e}')