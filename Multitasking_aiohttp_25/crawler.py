import aiohttp
import asyncio
import aiofiles
from bs4 import BeautifulSoup
from pathlib import Path

URL = 'https://habr.com/ru/articles/774514/'
depth = 5
OUT_PATH = (Path(__file__).parent / 'links').absolute()
OUT_PATH.mkdir(parents=True, exist_ok=True)
async def get_links(client: aiohttp.ClientSession, URL):

        async with client.get(URL) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            for link in soup.find_all('a'):
                if link.has_attr('href'):
                    await write_to_file(link['href'])

async def write_to_file(mylink):
    file_path = "{}/links.txt".format(OUT_PATH)
    async with aiofiles.open(file_path, mode='a') as f:
        await f.write(mylink + '\n')


async def get_all_links():
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(15)) as client:
        tasks = [get_links(client, URL) for _ in range(depth)]
        return await asyncio.gather(*tasks)


def main():
    res = asyncio.run(get_all_links())


if __name__ == "__main__":
    main()