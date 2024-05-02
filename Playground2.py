import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)


urls = ["http://www.gerozayas.com", "http://best-english-resources.pages.dev"]
result = asyncio.run(main(urls))

# print(result)
