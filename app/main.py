from app.functions.loading import load
from app.functions.init import init
from app.functions.data_treatment import treat
from app.database.connection import export
import asyncio

async def main():
    await asyncio.gather(
        export(treat(init())),
        load()
    )
    