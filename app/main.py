from app.loading import load
from app.init import init
from app.data_treatment import treat
import asyncio

async def main():
    await asyncio.gather(
        treat(init()),
        load()
    )
    