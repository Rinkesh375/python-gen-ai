import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt_call(data):
    return f" {data[::-1]}"


async def main():
    loop = asyncio.get_running_loop()
    with  ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool,encrypt_call,"Rinkesh987654321")
        print(f"{result} of encrypt call")
        
        
if __name__ == "__main__":
    asyncio.run(main())        


