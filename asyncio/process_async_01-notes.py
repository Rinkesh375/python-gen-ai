"""
==========================================================
Topic: asyncio + ProcessPoolExecutor
(Running CPU-Intensive Tasks in Separate Processes)
==========================================================

Code:
-----

import asyncio
from concurrent.futures import ProcessPoolExecutor


def encrypt_call(data):
    return f"{data[::-1]}"


async def main():

    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as pool:

        result = await loop.run_in_executor(
            pool,
            encrypt_call,
            "Rinkesh987654321"
        )

        print(f"{result} of encrypt call")


if __name__ == "__main__":
    asyncio.run(main())

==========================================================
What is this program?
==========================================================

Hinglish Explanation:
---------------------

Ye program ek CPU task ko

alag process me run karta hai.

Is example me

encrypt_call()

sirf string reverse kar raha hai.

IMPORTANT

Ye real encryption nahi hai.

Ye sirf ProcessPoolExecutor samjhane ke liye example hai.

English Explanation:
--------------------

This program executes a CPU-bound function

inside another process.

The encrypt_call()

function only reverses a string.

It is NOT real encryption.

The example is only for learning ProcessPoolExecutor.

==========================================================
Why ProcessPoolExecutor?
==========================================================

Hinglish Explanation:
---------------------

Python me CPU intensive work

Event Loop ko slow kar deta hai.

Agar heavy calculations

main process me chalenge

to baaki async tasks ruk jayenge.

ProcessPoolExecutor

alag Python process create karta hai.

Isliye heavy CPU work

background process me hota hai.

English Explanation:
--------------------

CPU-intensive work can block the event loop.

ProcessPoolExecutor runs CPU-heavy tasks

inside another Python process,

keeping the async application responsive.

==========================================================
Thread vs Process
==========================================================

Thread

✔ Same Memory

✔ Best for I/O

✔ API Calls

✔ Database

✔ File Reading

--------------------------------------

Process

✔ Separate Memory

✔ Separate Python Interpreter

✔ Best for CPU Work

✔ Image Processing

✔ AI

✔ Encryption

✔ Video Encoding

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
2. ProcessPoolExecutor
==========================================================

Code

from concurrent.futures import ProcessPoolExecutor

==========================================================

Hinglish Explanation:
---------------------

Ye multiple Python processes create karta hai.

Har process apna CPU core use kar sakta hai.

English Explanation:
--------------------

Creates a pool of worker processes.

Each process has its own Python interpreter.

==========================================================
3. def encrypt_call(data):
==========================================================

Hinglish Explanation:
---------------------

Ye ek normal synchronous function hai.

Ye async function nahi hai.

English Explanation:
--------------------

This is a normal synchronous function.

==========================================================
4. data[::-1]
==========================================================

Code

data[::-1]

==========================================================

Hinglish Explanation:
---------------------

Ye Python slicing hai.

String ko reverse karta hai.

Example

data = "Python"

Result

"nohtyP"

IMPORTANT

Ye encryption nahi hai.

English Explanation:
--------------------

This uses Python slicing.

It simply reverses the string.

It is NOT encryption.

==========================================================
5. asyncio.get_running_loop()
==========================================================

Code

loop = asyncio.get_running_loop()

==========================================================

Hinglish Explanation:
---------------------

Currently running event loop return karta hai.

Isi ke through

hum background process start karte hain.

English Explanation:
--------------------

Returns the currently running event loop.

==========================================================
6. ProcessPoolExecutor()
==========================================================

Code

with ProcessPoolExecutor() as pool:

==========================================================

Hinglish Explanation:
---------------------

Ye worker processes create karta hai.

Example

Main Process

↓

Worker Process 1

Worker Process 2

Worker Process 3

English Explanation:
--------------------

Creates reusable worker processes.

==========================================================
7. loop.run_in_executor()
==========================================================

Code

result = await loop.run_in_executor(

    pool,

    encrypt_call,

    "Rinkesh987654321"

)

==========================================================

Hinglish Explanation:
---------------------

Ye sabse important line hai.

Execution

Event Loop

↓

Background Process

↓

encrypt_call()

↓

Return Result

↓

Print

Main process free rehta hai.

English Explanation:
--------------------

Runs the blocking CPU function

inside another process.

The async event loop remains responsive.

Syntax

await loop.run_in_executor(

    executor,

    function,

    argument

)

==========================================================
8. await
==========================================================

Hinglish Explanation:
---------------------

await result ka wait karta hai.

Lekin event loop block nahi hota.

English Explanation:
--------------------

Waits for the process to finish

without blocking the event loop.

==========================================================
9. if __name__ == "__main__":
==========================================================

Hinglish Explanation:
---------------------

Ye bahut important line hai.

Especially

Windows me

ProcessPoolExecutor use karte waqt.

Iske bina

new processes baar baar

program ko dobara execute kar sakte hain.

English Explanation:
--------------------

This is required,

especially on Windows,

when using ProcessPoolExecutor.

Without it,

child processes may repeatedly execute the program.

==========================================================
Execution Flow
==========================================================

Program Starts
      │
      ▼
Event Loop Starts
      │
      ▼
Create Process Pool
      │
      ▼
run_in_executor()
      │
      ├──────────────────────────┐
      │                          │
      ▼                          ▼
Main Process             Worker Process
                               │
                               ▼
                  encrypt_call()
                               │
                               ▼
                     Reverse String
                               │
                               ▼
                     Return Result
                               │
      ◄────────────────────────┘
      │
      ▼
Print Result

==========================================================
Real Industry Use Cases
==========================================================

1. Password Hashing

User Login

↓

bcrypt.hash()

↓

CPU Intensive

↓

ProcessPoolExecutor

------------------------------------------

2. AI / Machine Learning

Upload Image

↓

Run AI Model

↓

Heavy CPU

↓

ProcessPoolExecutor

------------------------------------------

3. PDF Generation

Generate 500-page Report

↓

CPU Intensive

↓

Background Process

------------------------------------------

4. Image Compression

Upload Image

↓

Resize

↓

Compress

↓

Separate Process

------------------------------------------

5. Video Encoding

Upload Video

↓

Convert MP4

↓

Background Process

------------------------------------------

6. Pharma (Similar to Your Work)

Generate Drug Report

↓

Read 20,000 Records

↓

Generate Charts

↓

Create PDF

↓

Background Process

==========================================================
ThreadPool vs ProcessPool
==========================================================

ThreadPoolExecutor

✔ API Calls

✔ File Reading

✔ Database

✔ HTTP Requests

✔ Email Sending

------------------------------------------

ProcessPoolExecutor

✔ Image Processing

✔ AI

✔ Encryption

✔ Password Hashing

✔ PDF Generation

✔ Video Encoding

✔ Large Calculations

==========================================================
Better Real Example
==========================================================

Instead of reversing a string,

imagine generating a password hash.

def hash_password(password):

    import bcrypt

    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )

Hashing is CPU intensive.

It should run in ProcessPoolExecutor.

==========================================================
Interview Questions
==========================================================

Q1. Why ProcessPoolExecutor?

Ans:

To execute CPU-intensive work in another process.

----------------------------------------------------------

Q2. Why not ThreadPoolExecutor?

Ans:

Threads are best for I/O-bound work.

CPU-bound work benefits from separate processes because of Python's Global Interpreter Lock (GIL).

----------------------------------------------------------

Q3. Why is __name__ == "__main__" required?

Ans:

It prevents child processes from recursively starting the program, especially on Windows.

----------------------------------------------------------

Q4. When should you use ProcessPoolExecutor?

Ans:

✔ AI

✔ Password Hashing

✔ Image Processing

✔ Video Encoding

✔ PDF Generation

✔ Data Analysis

==========================================================
Key Points
==========================================================

✔ ProcessPoolExecutor creates worker processes.

✔ Best for CPU-intensive tasks.

✔ run_in_executor() runs the function in another process.

✔ await waits without blocking the event loop.

✔ __name__ == "__main__" is required for safe multiprocessing.

✔ String reversal is only a learning example, not real encryption.

==========================================================
End of Notes
==========================================================