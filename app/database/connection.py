import pandas as pd 
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
import asyncio

async def export_sql(db):
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