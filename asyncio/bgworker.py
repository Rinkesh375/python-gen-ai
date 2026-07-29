import threading
import time
import asyncio

def background_worker():
    while True:
        time.sleep(1)
        print(f"Logging the system health {time.time()}")
        
        
async def fetch_orders():
    await asyncio.sleep(3)
    print("Order Fetch")
    
threading.Thread(target=background_worker,daemon=True).start()
asyncio.run(fetch_orders())    
            