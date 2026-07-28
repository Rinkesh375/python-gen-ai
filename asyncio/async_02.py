import asyncio
import time


async def get_user_profile():
    print("Fetching User Profile...")
    await asyncio.sleep(2)
    print("✅ User Profile Loaded")
    return {
        "name": "Rinkesh",
        "email": "rinkesh@gmail.com"
    }


async def get_recent_orders():
    print("Fetching Orders...")
    await asyncio.sleep(2)
    print("✅ Orders Loaded")
    return [
        "iPhone 17",
        "Laptop",
        "Wireless Mouse"
    ]


async def get_wallet_balance():
    print("Fetching Wallet...")
    await asyncio.sleep(2)
    print("✅ Wallet Loaded")
    return 5600


async def get_notifications():
    print("Fetching Notifications...")
    await asyncio.sleep(2)
    print("✅ Notifications Loaded")
    return 12


async def main():

    start = time.time()

    profile, orders, wallet, notifications = await asyncio.gather(
        get_user_profile(),
        get_recent_orders(),
        get_wallet_balance(),
        get_notifications()
    )

    end = time.time()

    print("\n========== Dashboard ==========")
    print(profile)
    print(orders)
    print(wallet)
    print(notifications)

    print(f"\nTotal Time : {end-start:.2f} seconds")


asyncio.run(main())