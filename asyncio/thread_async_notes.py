"""
==========================================================
Topic: asyncio.run_in_executor() with ThreadPoolExecutor
==========================================================

Code:
-----

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def check_stock(item):
    print(f"Checking {item} in stock")
    time.sleep(3)
    return f"{item} stock: 42"


async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool,
            check_stock,
            "iPhone"
        )

        print(result)


asyncio.run(main())

==========================================================
What is this program?
==========================================================

Hinglish Explanation:
---------------------

Ye program ek blocking (normal) function ko asynchronous
program ke andar run karta hai.

Normally,

time.sleep()

program ko block kar deta hai.

Lekin run_in_executor()

us function ko ek alag thread me chala deta hai.

Isliye event loop block nahi hota.

English Explanation:
--------------------

This program runs a blocking function inside an async application.

Instead of blocking the event loop,

the blocking function executes in a separate thread.

This allows the async application to remain responsive.

==========================================================
Real Life Problem
==========================================================

Imagine:

You are building an E-commerce Website.

When user opens a product page,

you need to

✔ Fetch Product Details (Async API)

✔ Fetch Reviews (Async API)

✔ Check Warehouse Stock

Problem:

Warehouse software is old.

It only provides a blocking Python function.

Example:

check_stock()

uses

time.sleep()

or

Database Driver

or

Legacy Library

If you call it directly,

the whole async application freezes.

Solution:

run_in_executor()

==========================================================
1. import asyncio
==========================================================

Hinglish Explanation:
---------------------

asyncio asynchronous programming ke liye use hoti hai.

Ye event loop manage karti hai.

English Explanation:
--------------------

asyncio provides asynchronous programming support.

==========================================================
2. import time
==========================================================

Hinglish Explanation:
---------------------

time module ka use

time.sleep()

ke liye kiya gaya hai.

Ye blocking sleep hai.

English Explanation:
--------------------

time module provides time.sleep(),

which blocks the current thread.

==========================================================
3. ThreadPoolExecutor
==========================================================

Code
----

from concurrent.futures import ThreadPoolExecutor

==========================================================

Hinglish Explanation:
---------------------

ThreadPoolExecutor

multiple threads create karta hai.

Ye blocking functions ko background thread me run karta hai.

English Explanation:
--------------------

ThreadPoolExecutor creates a pool of worker threads.

Blocking functions can run inside these threads.

==========================================================
4. def check_stock(item):
==========================================================

Code
----

def check_stock(item):

==========================================================

Hinglish Explanation:
---------------------

Ye ek normal Python function hai.

Notice:

Ye async function nahi hai.

English Explanation:
--------------------

This is a normal synchronous Python function.

It is NOT asynchronous.

==========================================================
5. print(...)
==========================================================

print(f"Checking {item} in stock")

Hinglish Explanation:
---------------------

Ye batata hai ki warehouse me stock check ho raha hai.

Example Output

Checking iPhone in stock

English Explanation:
--------------------

Prints a message indicating stock checking has started.

==========================================================
6. time.sleep(3)
==========================================================

Code
----

time.sleep(3)

==========================================================

Hinglish Explanation:
---------------------

Ye thread ko 3 seconds ke liye rok deta hai.

IMPORTANT

Ye blocking sleep hai.

Agar ise async function ke andar directly use karenge,

to pura event loop block ho jayega.

English Explanation:
--------------------

time.sleep()

blocks the current thread.

If executed inside an async function,

it freezes the event loop.

Wrong Example
-------------

async def main():

    time.sleep(3)

Everything stops ❌

Correct

await asyncio.sleep(3)

or

run_in_executor()

==========================================================
7. return
==========================================================

return f"{item} stock: 42"

Hinglish Explanation:
---------------------

Warehouse se stock quantity return hoti hai.

English Explanation:
--------------------

Returns the available stock.

==========================================================
8. asyncio.get_running_loop()
==========================================================

Code
----

loop = asyncio.get_running_loop()

==========================================================

Hinglish Explanation:
---------------------

Ye currently running event loop ko return karta hai.

Isi event loop se hum background thread start karte hain.

English Explanation:
--------------------

Returns the currently running event loop.

==========================================================
9. ThreadPoolExecutor()
==========================================================

Code
----

with ThreadPoolExecutor() as pool:

==========================================================

Hinglish Explanation:
---------------------

Ye ek thread pool create karta hai.

Pool ka matlab

multiple reusable threads.

Thread ka kaam complete hone ke baad

automatically cleanup ho jata hai.

English Explanation:
--------------------

Creates a pool of reusable worker threads.

The pool is automatically cleaned up.

==========================================================
10. loop.run_in_executor()
==========================================================

Code
----

result = await loop.run_in_executor(
    pool,
    check_stock,
    "iPhone"
)

==========================================================

Hinglish Explanation:
---------------------

Ye sabse important line hai.

Is line me

pool

↓

Background Thread

check_stock

↓

Function

"iPhone"

↓

Argument

Execution

Event Loop
     │
     │
     ├───────────────► Background Thread
     │                     │
     │                     ▼
     │             check_stock("iPhone")
     │                     │
     │             time.sleep(3)
     │                     │
     │               Return Result
     │                     │
     ◄─────────────────────┘

Event loop wait karta hai

lekin block nahi hota.

English Explanation:
--------------------

run_in_executor()

runs the blocking function

inside a worker thread.

The async event loop remains free

to execute other tasks.

Syntax

await loop.run_in_executor(

    executor,

    function,

    argument

)

==========================================================
11. await
==========================================================

Hinglish Explanation:
---------------------

await result aane ka wait karta hai.

Lekin

event loop ko block nahi karta.

English Explanation:
--------------------

await waits for the thread to finish

without blocking the event loop.

==========================================================
12. print(result)
==========================================================

Output

iPhone stock: 42

Hinglish Explanation:
---------------------

Background thread ka returned value print hota hai.

English Explanation:
--------------------

Prints the value returned from the worker thread.

==========================================================
13. asyncio.run(main())
==========================================================

Hinglish Explanation:
---------------------

Program ka starting point.

Ye event loop start karta hai.

English Explanation:
--------------------

Starts the event loop and executes main().

==========================================================
Execution Flow
==========================================================

Program Starts
      │
      ▼
Event Loop Starts
      │
      ▼
Create Thread Pool
      │
      ▼
run_in_executor()
      │
      ├──────────────────────────┐
      │                          │
      ▼                          ▼
Event Loop                Background Thread
                               │
                               ▼
                   check_stock("iPhone")
                               │
                        time.sleep(3)
                               │
                               ▼
                    Return "iPhone stock:42"
                               │
      ◄────────────────────────┘
      │
      ▼
Print Result

==========================================================
Real Industry Use Cases
==========================================================

1. E-Commerce

Product Page

↓

Async API

↓

Check Warehouse Stock

↓

Old ERP System

↓

Blocking Function

Use

run_in_executor()

--------------------------------------------

2. Banking

Customer Login

↓

Async API

↓

Old Banking Software

↓

Blocking Database Driver

↓

run_in_executor()

--------------------------------------------

3. Pharma (Similar to Your Work)

Drug Dashboard

↓

Fetch Drug Details (Async)

↓

Fetch Clinical Trials (Async)

↓

Read Huge Excel File (Blocking)

↓

run_in_executor()

--------------------------------------------

4. Image Processing

User uploads image

↓

Resize Image

↓

Compress Image

↓

Blocking Library (Pillow/OpenCV)

↓

run_in_executor()

--------------------------------------------

5. PDF Generation

User clicks

Download Report

↓

Generate PDF

↓

Blocking Library (ReportLab)

↓

run_in_executor()

==========================================================
Example Without run_in_executor()
==========================================================

async def main():

    check_stock("iPhone")

Problem

time.sleep()

↓

Blocks Event Loop

↓

No other async task can execute

==========================================================
Example With run_in_executor()
==========================================================

async def main():

    await asyncio.gather(

        fetch_user(),

        fetch_orders(),

        loop.run_in_executor(
            pool,
            check_stock,
            "iPhone"
        )

    )

Now

User API

Orders API

Stock Checking

All execute together.

==========================================================
Interview Questions
==========================================================

Q1. Why use run_in_executor()?

Ans:

To execute blocking synchronous code without blocking the async event loop.

----------------------------------------------------------

Q2. Why ThreadPoolExecutor?

Ans:

It runs blocking I/O operations in separate threads.

----------------------------------------------------------

Q3. Can we use time.sleep() inside async?

Ans:

No.

Use

await asyncio.sleep()

or

run_in_executor().

----------------------------------------------------------

Q4. When should you use run_in_executor()?

Ans:

When working with legacy synchronous libraries such as:

✔ File Reading

✔ Image Processing

✔ PDF Generation

✔ Old Database Drivers

✔ ERP Systems

✔ Blocking Third-party SDKs

==========================================================
Key Points
==========================================================

✔ asyncio works best with non-blocking code.

✔ time.sleep() blocks the thread.

✔ ThreadPoolExecutor creates worker threads.

✔ run_in_executor() runs blocking code safely.

✔ Event loop remains responsive.

✔ Best for integrating old synchronous code into async applications.

==========================================================
End of Notes
==========================================================

"""