"""
==========================================================
Topic: Using Threading with Asyncio
==========================================================

Code:
-----

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


threading.Thread(
    target=background_worker,
    daemon=True
).start()

asyncio.run(fetch_orders())

==========================================================
What is this Program?
==========================================================

Hinglish Explanation:
---------------------

Ye program ek hi time par

1. Background me continuously system health monitor karta hai.

Aur

2. Async function se orders fetch karta hai.

Matlab

Thread

↓

Background Logging

Aur

Asyncio

↓

Order Fetching

Dono ek saath chal rahe hain.

English Explanation:
--------------------

This program performs two tasks simultaneously.

Thread

↓

Runs a background health monitor.

Asyncio

↓

Fetches orders asynchronously.

Both work together without interfering with each other.

==========================================================
Real Industry Scenario
==========================================================

Imagine Amazon Server

Customer opens Dashboard.

At the same time

Background Thread

↓

✔ CPU Usage

✔ RAM Usage

✔ Health Logs

✔ Server Monitoring

Asyncio

↓

✔ Fetch Orders

✔ Fetch Products

✔ Fetch Notifications

Background monitoring never stops,

while async requests continue serving users.

==========================================================
1. import threading
==========================================================

Hinglish Explanation:
---------------------

threading module

multiple threads create karne ke liye use hota hai.

Ek thread background me kaam kar sakta hai,

jabki main thread apna kaam karta rehta hai.

English Explanation:
--------------------

threading is used to create multiple threads.

Each thread can execute independently.

==========================================================
2. import time
==========================================================

Hinglish Explanation:
---------------------

time.sleep()

aur

time.time()

use karne ke liye.

English Explanation:
--------------------

Provides

time.sleep()

and

time.time().

==========================================================
3. import asyncio
==========================================================

Hinglish Explanation:
---------------------

asyncio

network,

API,

database,

I/O operations

ko efficiently handle karti hai.

English Explanation:
--------------------

asyncio is used for asynchronous I/O operations.

==========================================================
4. background_worker()
==========================================================

Code

def background_worker():

==========================================================

Hinglish Explanation:
---------------------

Ye normal synchronous function hai.

Ye background thread me chalega.

English Explanation:
--------------------

This is a normal synchronous function.

It runs inside a background thread.

==========================================================
5. while True
==========================================================

Code

while True:

==========================================================

Hinglish Explanation:
---------------------

Infinite loop.

Ye tab tak chalega

jab tak program band nahi hota.

English Explanation:
--------------------

Creates an infinite loop.

It runs until the program exits.

==========================================================
6. time.sleep(1)
==========================================================

Code

time.sleep(1)

==========================================================

Hinglish Explanation:
---------------------

Thread

1 second ke liye wait karega.

Fir dobara log print karega.

English Explanation:
--------------------

Pauses the thread for one second.

==========================================================
7. time.time()
==========================================================

Code

time.time()

==========================================================

Hinglish Explanation:
---------------------

Current Unix Timestamp return karta hai.

Example

1753856753.23

English Explanation:
--------------------

Returns the current Unix timestamp.

==========================================================
8. async def fetch_orders()
==========================================================

Hinglish Explanation:
---------------------

Ye async function hai.

Ye server se orders fetch kar raha hai.

English Explanation:
--------------------

This coroutine simulates fetching orders.

==========================================================
9. await asyncio.sleep(3)
==========================================================

Hinglish Explanation:
---------------------

3 second ka network delay simulate karta hai.

IMPORTANT

Ye event loop ko block nahi karta.

English Explanation:
--------------------

Simulates a network request.

Does NOT block the event loop.

==========================================================
10. threading.Thread()
==========================================================

Code

threading.Thread(

    target=background_worker,

    daemon=True

)

==========================================================

Hinglish Explanation:
---------------------

Ye naya thread create karta hai.

target

↓

Kaunsa function chalega.

daemon=True

↓

Background thread.

Main program band hote hi

ye automatically band ho jayega.

English Explanation:
--------------------

Creates a new thread.

target

Specifies the function.

daemon=True

Creates a daemon thread,

which exits automatically when the main program exits.

==========================================================
11. .start()
==========================================================

Code

.start()

==========================================================

Hinglish Explanation:
---------------------

Thread ko start karta hai.

Ab

background_worker()

parallel me chalna start karega.

English Explanation:
--------------------

Starts the thread.

==========================================================
12. asyncio.run(fetch_orders())
==========================================================

Hinglish Explanation:
---------------------

Event loop start hota hai.

fetch_orders()

execute hota hai.

English Explanation:
--------------------

Starts the event loop

and executes fetch_orders().

==========================================================
Execution Flow
==========================================================

Program Starts
        │
        ▼
Start Background Thread
        │
        ▼
Logging Every 1 Second
        │
        │
        ├──────────────────────────────┐
        │                              │
        ▼                              ▼
Background Thread               Async Event Loop
        │                              │
        │                              ▼
        │                     Fetch Orders
        │                              │
        │                     Wait 3 Seconds
        │                              │
        ▼                              ▼
Logging...                     Order Fetch
Logging...
Logging...

==========================================================
Expected Output
==========================================================

Logging the system health 1753856001

Logging the system health 1753856002

Logging the system health 1753856003

Order Fetch

==========================================================
Why daemon=True?
==========================================================

Without daemon

Background thread

↓

Never Stops

↓

Program Never Ends

With daemon=True

Main Program Ends

↓

Background Thread Ends Automatically

==========================================================
Real Industry Use Cases
==========================================================

1. Web Server Monitoring

Background Thread

↓

Log CPU Usage

↓

Log Memory Usage

↓

Health Checks

-----------------------------------------

2. Pharma Dashboard (Like Your Work)

Background Thread

↓

Refresh Cache

↓

Log API Response Time

↓

Check Database Health

Asyncio

↓

Fetch Drug Data

↓

Fetch News

↓

Fetch Conferences

-----------------------------------------

3. Banking

Background Thread

↓

Transaction Logger

↓

Fraud Monitor

Asyncio

↓

Customer APIs

-----------------------------------------

4. Gaming Server

Background Thread

↓

Player Health Check

↓

Save Logs

Asyncio

↓

Receive Player Actions

==========================================================
Thread vs Asyncio
==========================================================

Thread

✔ Background Work

✔ Monitoring

✔ Logging

✔ File Watching

✔ Scheduler

----------------------------------------

Asyncio

✔ API Calls

✔ Database

✔ HTTP Requests

✔ WebSocket

✔ File Upload

==========================================================
Better Real Example
==========================================================

Imagine a Food Delivery App

Background Thread

↓

Check Driver GPS

↓

Write Logs

↓

Monitor Server

Asyncio

↓

Fetch Restaurants

↓

Fetch Orders

↓

Process Payments

Both run together.

==========================================================
Interview Questions
==========================================================

Q1. Why use threading here?

Ans:

To continuously run a background task independently.

----------------------------------------------------

Q2. Why daemon=True?

Ans:

So the thread exits automatically when the main program finishes.

----------------------------------------------------

Q3. Can Threading and Asyncio work together?

Ans:

Yes.

Threading handles background synchronous work.

Asyncio handles asynchronous I/O operations.

----------------------------------------------------

Q4. What happens without daemon=True?

Ans:

The background thread keeps running,

so the program does not terminate.

==========================================================
Key Points
==========================================================

✔ Thread runs independently.

✔ daemon=True creates a background thread.

✔ asyncio handles asynchronous tasks.

✔ Both can run together.

✔ Threads are good for monitoring and logging.

✔ Asyncio is best for APIs and network I/O.

==========================================================
End of Notes
==========================================================