from app.functions.loading import load
from app.functions.init import init
from app.functions.data_treatment import treat
import asyncio

async def main():
    await asyncio.gather(
        treat(init()),
        load()
    )
    