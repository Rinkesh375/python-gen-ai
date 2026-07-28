"""
==========================================================
Topic: asyncio.gather() - Run Multiple Async Tasks Together
==========================================================

Code:
-----

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

    print(f"Total Time: {end - start:.2f} seconds")


asyncio.run(main())

==========================================================
1. import time
==========================================================

Hinglish Explanation:
---------------------
"time" module ko program ka execution time measure karne ke liye use karte hain.

Is example me:
- start time record karte hain.
- End me finish time record karte hain.
- Dono ka difference nikal kar dekhte hain kitna time laga.

English Explanation:
--------------------
The "time" module is used to measure how long the program takes to execute.

Example:
--------
import time

start = time.time()

# some work

end = time.time()

print(end - start)

==========================================================
2. import asyncio
==========================================================

Hinglish Explanation:
---------------------
asyncio Python ki built-in library hai jo asynchronous programming ke liye use hoti hai.

Ye ek hi thread me multiple I/O tasks ko efficiently handle karti hai.

English Explanation:
--------------------
asyncio is Python's built-in library for asynchronous programming.

It allows multiple I/O operations to run efficiently without blocking.

==========================================================
3. async def getting_data_server(data_name):
==========================================================

Hinglish Explanation:
---------------------
"async def" ka matlab hai ye ek asynchronous function hai.

Ye function future me pause bhi ho sakta hai aur baad me wahi se continue ho sakta hai.

Is function ka kaam server se data fetch karna simulate karna hai.

English Explanation:
--------------------
"async def" creates a coroutine function.

It can pause execution and resume later without blocking other tasks.

Example:
--------
async def hello():
    print("Hello")

==========================================================
4. print(...)
==========================================================

print(f"start fetching the data from server for {data_name}")

Hinglish Explanation:
---------------------
Ye sirf batata hai ki data fetch hona start ho gaya.

Agar data_name "User lists" hai to output hoga:

start fetching the data from server for User lists

English Explanation:
--------------------
This prints a message indicating that fetching has started.

==========================================================
5. await asyncio.sleep(2)
==========================================================

Hinglish Explanation:
---------------------
Ye line sabse important hai.

Normally:

time.sleep(2)

Program ko completely rok deta hai.

Lekin:

await asyncio.sleep(2)

Sirf current coroutine ko pause karta hai.

Is duration me asyncio dusre tasks ko execute kar deta hai.

Yahi asynchronous programming ka main benefit hai.

English Explanation:
--------------------
await pauses only the current coroutine.

The event loop continues executing other async tasks.

Example:
--------
await asyncio.sleep(3)

Means:
Pause this task for 3 seconds while other tasks continue.

==========================================================
6. print(...)
==========================================================

print(f"fetched the data from server for {data_name}")

Hinglish Explanation:
---------------------
2 second complete hone ke baad ye print hota hai.

English Explanation:
--------------------
This message is printed after the simulated server response is complete.

==========================================================
7. async def main():
==========================================================

Hinglish Explanation:
---------------------
Ye hamara main async function hai.

Saare async operations isi function ke andar likhe jaate hain.

English Explanation:
--------------------
This is the main coroutine that controls all asynchronous work.

==========================================================
8. start = time.time()
==========================================================

Hinglish Explanation:
---------------------
Program start hone ka current timestamp store hota hai.

English Explanation:
--------------------
Stores the current timestamp before execution begins.

==========================================================
9. await asyncio.gather(...)
==========================================================

Code:
-----

await asyncio.gather(
    getting_data_server("User lists"),
    getting_data_server("Product Orders"),
    getting_data_server("Transaction Amounts")
)

==========================================================

Hinglish Explanation:
---------------------

Ye line ek saath multiple async functions ko start karti hai.

Important:

❌ Pehla complete hone ka wait nahi karti.

Sabhi tasks almost same time par start ho jaate hain.

Visual:

Time

0 sec

Task1 ---- waiting ------------ done

Task2 ---- waiting ------------ done

Task3 ---- waiting ------------ done

Sabhi 2 second wait kar rahe hain ek hi time par.

Isliye total time ≈ 2 seconds.

Agar gather use nahi karte:

await getting_data_server("User")
await getting_data_server("Orders")
await getting_data_server("Transactions")

Tab:

Task1 → 2 sec

Task2 → 2 sec

Task3 → 2 sec

Total = 6 sec

English Explanation:
--------------------

asyncio.gather() schedules multiple coroutines to run concurrently.

It waits until all of them finish.

Without gather:

Task1
↓

Task2
↓

Task3

Total = 6 seconds

With gather:

Task1
Task2
Task3

Run together.

Total ≈ 2 seconds.

==========================================================
10. end = time.time()
==========================================================

Hinglish Explanation:
---------------------
Sabhi tasks complete hone ke baad current time record hota hai.

English Explanation:
--------------------
Stores the finish timestamp after all async tasks complete.

==========================================================
11. print(end - start)
==========================================================

Hinglish Explanation:
---------------------
Ye total execution time print karta hai.

Expected output:

2.00 seconds

English Explanation:
--------------------
Prints the total execution time.

==========================================================
12. asyncio.run(main())
==========================================================

Hinglish Explanation:
---------------------
Ye program ka starting point hai.

Ye event loop create karta hai.

Fir main() coroutine ko run karta hai.

Aur end me event loop automatically close kar deta hai.

English Explanation:
--------------------
asyncio.run() starts the event loop, executes the main coroutine,
and closes the loop when finished.

Example:
--------
asyncio.run(main())

==========================================================
Execution Flow
==========================================================

Program Starts
       │
       ▼
asyncio.run(main())
       │
       ▼
Record Start Time
       │
       ▼
asyncio.gather()
       │
       ├──────────────┐
       │              │
       ▼              ▼
User Lists      Product Orders
       │              │
       └──────┐       │
              ▼       ▼
      Transaction Amounts
              │
       (All wait together)
              │
              ▼
     All Finish Together
              │
              ▼
 Record End Time
              │
              ▼
 Print Total Time

==========================================================
Output
==========================================================

start fetching the data from server for User lists
start fetching the data from server for Product Orders
start fetching the data from server for Transaction Amounts

(2 seconds later)

fetched the data from server for User lists
fetched the data from server for Product Orders
fetched the data from server for Transaction Amounts

Total Time: 2.00 seconds

==========================================================
Key Points
==========================================================

✔ async def creates a coroutine.

✔ await pauses only the current coroutine.

✔ asyncio.sleep() is non-blocking.

✔ asyncio.gather() runs multiple async tasks concurrently.

✔ Total execution time equals approximately the longest task,
not the sum of all task times.

✔ asyncio.run() starts and manages the event loop.

==========================================================
Interview Questions
==========================================================

Q1. What is asyncio.gather()?
Ans:
Runs multiple async tasks concurrently and waits for all to finish.

Q2. Difference between time.sleep() and asyncio.sleep()?

time.sleep():
- Blocks the entire thread.

asyncio.sleep():
- Pauses only the current coroutine.

Q3. Why is gather() faster here?

Because all three tasks wait at the same time instead of one after another.

Q4. Why is total time about 2 seconds instead of 6?

Because the three 2-second waits overlap and execute concurrently.

==========================================================
End of Notes
==========================================================


"""