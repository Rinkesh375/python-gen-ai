"""
====================================================================
        Threads vs Processes (Real World Examples)
====================================================================

Author : Your Python Notes

====================================================================
What is a Thread?
====================================================================

Hinglish
---------

Thread ek lightweight worker hota hai.

Ek hi Python application ke andar
multiple threads kaam karte hain.

Sab threads same memory share karte hain.

English
--------

A thread is a lightweight worker
inside one Python process.

Multiple threads share the same memory.

====================================================================
What is a Process?
====================================================================

Hinglish
---------

Process ek independent Python program hota hai.

Har process ki apni

✔ Memory

✔ Variables

✔ Resources

hoti hain.

English
--------

A process is an independent Python program.

Each process has its own memory.

====================================================================
When to Use Threading?
====================================================================

Use threading when your program spends
most of its time WAITING.

Examples

✔ API Calls

✔ Database Queries

✔ Reading Files

✔ Sending Emails

✔ Uploading Files

✔ Downloading Files

✔ Chat Applications

Because these are

I/O Bound Tasks.

====================================================================
Real Example 1
Sending Emails
====================================================================

Imagine

100 users

Without Threads

User1

↓

Wait 2 sec

↓

User2

↓

Wait

↓

User3

Total

Very Slow

------------------------------------------------------------

With Threads

Thread1

↓

Email User1

Thread2

↓

Email User2

Thread3

↓

Email User3

All execute together.

This is exactly how
email systems work.

Example

import threading

def send_email(user):
    print(f"Sending email to {user}")

users = ["John","Alice","Bob"]

for user in users:

    thread = threading.Thread(
        target=send_email,
        args=(user,)
    )

    thread.start()

====================================================================
Real Example 2
Downloading Files
====================================================================

Imagine downloading

movie.mp4

song.mp3

python.pdf

Without Threads

Download

↓

Wait

↓

Download

↓

Wait

↓

Download

With Threads

All downloads start together.

Exactly how browsers work.

====================================================================
Real Example 3
API Requests
====================================================================

Suppose

Dashboard loads

Products

Orders

Customers

Invoices

Without Threads

Request Products

↓

Wait

↓

Orders

↓

Wait

↓

Customers

↓

Wait

Very slow.

------------------------------------------------------------

With Threads

Products

Orders

Customers

Invoices

All requested together.

Much faster.

====================================================================
When to Use Multiprocessing?
====================================================================

Use multiprocessing

when the CPU is doing
heavy calculations.

Examples

✔ AI Training

✔ Image Processing

✔ Video Rendering

✔ Password Hashing

✔ Data Analysis

✔ CSV Processing

✔ Scientific Calculations

These are

CPU Bound Tasks.

====================================================================
Real Example 1
Image Processing
====================================================================

Suppose

5000 Images

Need

Resize

Compress

Convert

Without Processes

Image1

↓

Image2

↓

Image3

↓

5000

Very Slow.

------------------------------------------------------------

With Processes

CPU Core1

↓

Images 1-1250

CPU Core2

↓

Images 1251-2500

CPU Core3

↓

Images 2501-3750

CPU Core4

↓

Images 3751-5000

Much Faster.

====================================================================
Real Example 2
Large CSV Files
====================================================================

Suppose

sales_january.csv

sales_february.csv

sales_march.csv

sales_april.csv

Each contains

5 Million Rows.

Without Processes

January

↓

February

↓

March

↓

April

------------------------------------------------------------

With Processes

Process1

↓

January

Process2

↓

February

Process3

↓

March

Process4

↓

April

All processed simultaneously.

====================================================================
Real Example 3
Your Pharma Project
====================================================================

Imagine

clinical_trials_2024.csv

clinical_trials_2025.csv

conference.csv

drug_master.csv

Each file

2 Million Records.

Every process

Reads

↓

Filters

↓

Validates

↓

Stores in Database

All files processed
at the same time.

====================================================================
Thread vs Process
====================================================================

Thread

✔ Lightweight

✔ Shared Memory

✔ Fast

✔ Used for Waiting Tasks

------------------------------------------------------------

Process

✔ Heavyweight

✔ Separate Memory

✔ Slower to Create

✔ Uses Multiple CPU Cores

====================================================================
JavaScript Comparison
====================================================================

JavaScript

fetch()

↓

Promise.all()

≈

Python Threading

------------------------------------------------------------

Node Worker Threads

↓

Python Thread

------------------------------------------------------------

Node child_process.fork()

↓

Python multiprocessing.Process

====================================================================
Interview Questions
====================================================================

Q

When should you use Threads?

Answer

For I/O-bound tasks

like

API

Database

Files

Emails

------------------------------------------------------------

Q

When should you use Processes?

Answer

For CPU-intensive tasks

like

AI

Image Processing

Machine Learning

Video Rendering

Large Calculations

------------------------------------------------------------

Q

Can Threads speed up CPU work?

Answer

Generally No.

Because of Python GIL.

Use Multiprocessing.

====================================================================
Golden Rule
====================================================================

Waiting?

↓

Threading

----------------------------------

Heavy Calculation?

↓

Multiprocessing

----------------------------------

Simple Program?

↓

No Need for Either

====================================================================
End of Notes
====================================================================

"""