from app.loading import load
from app.init import init
import asyncio

async def main():
    await asyncio.gather(
        init(),
        load()
    )