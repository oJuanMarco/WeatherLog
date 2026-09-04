import pandas as pd 
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from app.database.report import report
import asyncio
import questionary

async def export(db):
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