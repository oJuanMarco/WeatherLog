import pandas as pd
import asyncio

def report(db):
    try:
        db.loc[0,'temperatura_media_semanal'] = db['temperatura_media'].mean()
        db['temperatura_media_semanal'] = db['temperatura_media_semanal'].round(2)
        db.loc[0,'sensacao_termica_media_semanal'] = db['sensacao_termica_media'].mean()
        db['sensacao_termica_media_semanal'] = db['sensacao_termica_media_semanal'].round(2)
        db.loc[0,'volume_de_chuva_semanal_previsto'] = db['volume_de_chuva(mm)'].sum()
        db.loc[0,'maxima_semanal'] = db['maxima'].max()
        db.loc[0,'minima_semanal'] = db['minima'].min()

        db.fillna('').to_csv('weather_report.csv', index=False)

    except asyncio.TimeoutError as e:
        print(f'Limite de tempo atingido para execução: {e}')
    except asyncio.CancelledError as e:
        print(f'Task cancelada antes da execução: {e}')
    except asyncio.InvalidStateError as e:
        print(f'Operação inválida no estado de execução: {e}')
    except FileNotFoundError as e:
        print(f'Operação de report em falha por não encontrar o arquivo: {e}')
    except Exception as e:
        print(f'Ocorreu um erro inesperado em report: {e}')