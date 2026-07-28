import time
import asyncio

async def getting_data_server(data_name):
    print(f"start fetching the data from server for {data_name}")
    await asyncio.sleep(2)
    print(f"fetched the data from server for {data_name}")



async def main():
    start = time.time()
    await asyncio.gather(
        getting_data_server("User lists"),
        getting_data_server("Product Orders"),
        getting_data_server("Transaction Amounts")

    )    
    end = time.time()
    
    print(f"{end-start}")
    
    
asyncio.run(main())    