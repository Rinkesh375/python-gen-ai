import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


# Blocking function (Legacy ERP)
def check_stock(product_id):
    print("Checking warehouse stock...")
    time.sleep(3)
    return {"stock": 42}


# Async API
async def get_product():
    await asyncio.sleep(2)
    return {"name": "iPhone 17 Pro"}


# Async API
async def get_user():
    await asyncio.sleep(1)
    return {"user": "Rinkesh"}


async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        user, product, stock = await asyncio.gather(
            get_user(),
            get_product(),
            loop.run_in_executor(pool, check_stock, 101)
        )

        print(user)
        print(product)
        print(stock)


asyncio.run(main())