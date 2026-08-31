import pandas as pd
from app.init import init
import asyncio

def treat(db):

    for column in db.columns:
        if db[column].dtype == "datetime64[s, America/Sao_Paulo]":
            db[column] = db[column].astype(str).str.replace("-","/").apply(lambda x: x[:10])
            print(f"{column}:{db[column].dtype}")
        else:
            print(f"{column}:{db[column].dtype}")

    print(db)