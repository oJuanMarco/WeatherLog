from app.functions.loading import load
from app.functions.init import init
from app.functions.data_treatment import treat
from app.database.connection import export
import asyncio
# função de gerenciamento de código, definindo a ordem de chamada conforme seu andamento
async def main():
    try:
        await asyncio.gather(
            export(treat(init())),
            load()
        )
        
    except asyncio.TimeoutError as e:
        print(f'Limite de tempo atingido para execução: {e}')
    except asyncio.CancelledError as e:
        print(f'Task cancelada antes da execução: {e}')
    except asyncio.InvalidStateError as e:
        print(f'Operação inválida no estado de execução: {e}')
    except Exception as e:
        print(f'Erro ao executar main: {e}')