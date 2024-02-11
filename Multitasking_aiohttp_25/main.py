import asyncio
from pathlib import Path
import os
import aiohttp
import aiofiles

URL = 'https://cataas.com/cat'
CATS_WE_WANT = 10
OUT_PATH = (Path(__file__).parent / 'cats').absolute()
OUT_PATH.mkdir(parents=True, exist_ok=True)
async def get_cat(client: aiohttp.ClientSession, idx: int) -> bytes:

    async with client.get(URL) as response:
        print(response.status)
        result = await response.read()
        await write_to_disc(result, idx)


async def write_to_disc(content: bytes, id: int):
    file_path = "{}/{}.png".format(OUT_PATH, id)
    async with aiofiles.open(file_path, mode='wb') as f:
        await f.write(content)

async def get_all_cats():

    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(15)) as client:
        tasks = [get_cat(client, i) for i in range(CATS_WE_WANT)]
        return await asyncio.gather(*tasks)

def main():
    res = asyncio.run(get_all_cats())
    print(len(res))


if __name__ == "__main__":
    main()