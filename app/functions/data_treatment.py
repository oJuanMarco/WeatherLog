import pandas as pd
from app.functions.init import init
import asyncio

async def treat(db):
    db = await db

    for column in db.columns:
        if db[column].dtype == "datetime64[s, America/Sao_Paulo]":
            db[column] = db[column].astype(str).str.replace("-","/").apply(lambda x: x[:10])
        else:
            db[column] = db[column].astype(str).apply(lambda x: x[:4])
            db[column] = db[column].astype(float)

    print(db)
    return db