"""
==========================================================
Topic: Fetch Multiple URLs Concurrently using aiohttp
==========================================================

Code:
-----

import asyncio
import aiohttp


async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetch {url} with status: {response.status}")


async def main():
    urls = ["https://httpbin.org/delay/2"] * 3

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]

        await asyncio.gather(*tasks)


asyncio.run(main())

==========================================================
What is this program?
==========================================================

Hinglish Explanation:
---------------------

Ye program internet par ek website ko 3 baar request bhejta hai.

Sabhi requests ek saath (concurrently) bheji jaati hain.

Har request ko complete hone me 2 second lagte hain.

Lekin kyunki sabhi ek saath chalti hain,
total time lagbhag 2 seconds hi hota hai.

English Explanation:
--------------------

This program sends three HTTP requests to the same website.

All requests are executed concurrently.

Each request takes about 2 seconds.

Since they run together, the total execution time is about 2 seconds.

==========================================================
1. import asyncio
==========================================================

Hinglish Explanation:
---------------------

asyncio asynchronous programming ke liye use hoti hai.

Ye multiple I/O operations ko efficiently handle karti hai.

English Explanation:
--------------------

asyncio is Python's built-in library for asynchronous programming.

It allows multiple I/O operations to execute concurrently.

==========================================================
2. import aiohttp
==========================================================

Hinglish Explanation:
---------------------

aiohttp ek asynchronous HTTP library hai.

Ye internet par API call ya website request bhejne ke liye use hoti hai.

Ye requests ko non-blocking way me execute karti hai.

English Explanation:
--------------------

aiohttp is an asynchronous HTTP client library.

It allows sending HTTP requests without blocking the program.

Real Examples:
--------------

✔ REST APIs

✔ Weather API

✔ GitHub API

✔ OpenAI API

✔ Payment Gateway API

==========================================================
3. async def fetch_url(session, url):
==========================================================

Hinglish Explanation:
---------------------

Ye function ek website ko request bhejta hai.

Parameters:

session
↓

Current HTTP session

url
↓

Website address

English Explanation:
--------------------

This coroutine sends an HTTP request to a given URL.

Parameters:

session

HTTP Client Session

url

Website URL

==========================================================
4. async with session.get(url)
==========================================================

Code
----

async with session.get(url) as response:

==========================================================

Hinglish Explanation:
---------------------

Ye line website ko GET request bhejti hai.

Request complete hone tak coroutine pause ho jaati hai.

Baaki async tasks tab tak continue hote rehte hain.

Request complete hone ke baad response variable me data aa jata hai.

English Explanation:
--------------------

This sends an HTTP GET request.

While waiting for the server response,

the coroutine pauses,

allowing other async tasks to continue.

After completion,

the response object contains the server response.

Visual

Program
   │
   ▼
Send HTTP Request
   │
Waiting...
   │
Other Async Tasks Run
   │
Response Received

==========================================================
5. response.status
==========================================================

Code
----

response.status

==========================================================

Hinglish Explanation:
---------------------

Ye website ka HTTP Status Code return karta hai.

Examples:

200

Request successful

404

Page not found

500

Server error

English Explanation:
--------------------

Returns the HTTP Status Code.

Common Codes:

200 → Success

404 → Not Found

500 → Internal Server Error

==========================================================
6. urls = ["https://httpbin.org/delay/2"] * 3
==========================================================

Hinglish Explanation:
---------------------

Ye list me same URL ko 3 baar store karta hai.

Equivalent:

urls = [
    "...",
    "...",
    "..."
]

Ye website intentionally 2 second wait karti hai.

Isliye async difference clearly dikhta hai.

English Explanation:
--------------------

Creates a list containing the same URL three times.

The endpoint waits 2 seconds before responding.

==========================================================
7. aiohttp.ClientSession()
==========================================================

Code
----

async with aiohttp.ClientSession() as session:

==========================================================

Hinglish Explanation:
---------------------

Session ek browser ki tarah hota hai.

Har request ke liye naya connection banana expensive hota hai.

Isliye ek hi session reuse kiya jata hai.

Ye performance improve karta hai.

English Explanation:
--------------------

A ClientSession manages HTTP connections.

Instead of creating a new connection for every request,

the same session is reused,

which improves performance.

==========================================================
8. List Comprehension
==========================================================

Code
----

tasks = [
    fetch_url(session, url)
    for url in urls
]

==========================================================

Hinglish Explanation:
---------------------

Ye loop 3 coroutine objects banata hai.

Dhyan rahe,

Ye abhi execute nahi hote.

Sirf ready hote hain.

tasks =

Task1

Task2

Task3

English Explanation:
--------------------

Creates three coroutine objects.

They are NOT running yet.

Execution starts only when asyncio.gather() is called.

==========================================================
9. await asyncio.gather(*tasks)
==========================================================

Hinglish Explanation:
---------------------

Ye sabse important line hai.

*tasks

List ko alag-alag arguments me convert karta hai.

Matlab:

asyncio.gather(
    task1,
    task2,
    task3
)

Sabhi requests ek saath start hoti hain.

English Explanation:
--------------------

asyncio.gather() executes all coroutine objects concurrently.

The * operator unpacks the list.

Example:

tasks = [a, b, c]

↓

asyncio.gather(*tasks)

becomes

asyncio.gather(a, b, c)

==========================================================
10. asyncio.run(main())
==========================================================

Hinglish Explanation:
---------------------

Ye event loop start karta hai.

main() coroutine execute karta hai.

Program complete hone par event loop close ho jata hai.

English Explanation:
--------------------

Starts the asyncio event loop,

runs main(),

and closes the loop automatically.

==========================================================
Execution Flow
==========================================================

Program Starts
      │
      ▼
Create HTTP Session
      │
      ▼
Create 3 Coroutine Objects
      │
      ▼
asyncio.gather()
      │
      ├──────────────┐
      │              │
      ▼              ▼
Request 1      Request 2
      │              │
      └──────┐       │
             ▼       ▼
          Request 3
             │
     Waiting for Server
             │
             ▼
 All Responses Received
             │
             ▼
 Print Status Codes

==========================================================
Expected Output
==========================================================

Fetch https://httpbin.org/delay/2 with status: 200

Fetch https://httpbin.org/delay/2 with status: 200

Fetch https://httpbin.org/delay/2 with status: 200

==========================================================
Real Industry Example
==========================================================

Imagine you're building a News Dashboard.

When the page opens,

it needs data from multiple APIs.

news = await asyncio.gather(

    fetch_latest_news(),

    fetch_weather(),

    fetch_stock_market(),

    fetch_crypto_prices(),

    fetch_sports_scores()

)

Instead of waiting:

News

↓

Weather

↓

Stocks

↓

Crypto

↓

Sports

All APIs are requested together,

making the dashboard much faster.

==========================================================
Interview Questions
==========================================================

Q1. Why use aiohttp instead of requests?

Ans:

requests is synchronous (blocking).

aiohttp is asynchronous (non-blocking).

----------------------------------------------------------

Q2. Why use ClientSession()?

Ans:

To reuse HTTP connections and improve performance.

----------------------------------------------------------

Q3. Why use asyncio.gather()?

Ans:

To execute multiple HTTP requests concurrently.

----------------------------------------------------------

Q4. What does *tasks mean?

Ans:

It unpacks the list into separate arguments.

Example:

[a, b, c]

↓

func(*list)

↓

func(a, b, c)

----------------------------------------------------------

Q5. Why is this faster?

Ans:

Because all HTTP requests wait for the server at the same time instead of one after another.

==========================================================
Key Points
==========================================================

✔ aiohttp is used for asynchronous HTTP requests.

✔ ClientSession reuses HTTP connections.

✔ session.get() sends an HTTP GET request.

✔ async with automatically closes resources.

✔ response.status gives the HTTP status code.

✔ List comprehension creates coroutine objects.

✔ asyncio.gather() executes all requests concurrently.

✔ *tasks unpacks a list into individual arguments.

✔ This pattern is widely used in FastAPI, web scraping, API integrations, microservices, and backend systems.

==========================================================
End of Notes
==========================================================

"""