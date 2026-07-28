import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        return {
            "url": url,
            "status": response.status
        }

async def main():
    urls = ["https://httpbin.org/delay/2"] * 3

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

        print("\nResults:")
        for result in results:
            print(result)

asyncio.run(main())