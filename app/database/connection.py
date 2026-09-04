import pandas as pd 
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from app.database.report import report
import asyncio
import questionary
# define conexão de dados tratados e instancia tabela para um data_base em mySQL, além de realizar a chamada pra export em CSV
async def export(db):
    try:
        db = await db

        load_dotenv()

        db_url = os.getenv("DATABASE_URL")
        engine = create_engine(db_url)

        db.to_sql(
        name='resumo_semanal',    
        con=engine,            
        if_exists='replace',   
        index=False            
        )

        print("\nDados registrados para consulta em MySQL")

        report_export = await questionary.select("\nDeseja exportar o relatório?", choices=['Sim','Não']).ask_async()

        if report_export == "Não":
            print("Relatório não exportado")
        else:
            report(db)
            print("Relatório exportado com sucesso!")
    
    except asyncio.TimeoutError as e:
        print(f'Limite de tempo atingido para execução: {e}')
    except asyncio.CancelledError as e:
        print(f'Task cancelada antes da execução: {e}')
    except asyncio.InvalidStateError as e:
        print(f'Operação inválida no estado de execução: {e}')
    except FileNotFoundError as e:
        print(f'Operação de export em falha por não encontrar o arquivo: {e}')
    except Exception as e:
        print(f'Ocorreu um erro inesperado em export: {e}')
