"""
====================================================================
        Thread Lock (Race Condition) in Python
====================================================================

Author : Your Python Learning Notes

====================================================================
What is this program trying to do?
====================================================================

Hinglish
---------

Ye program 10 threads banata hai.

Har thread counter ko

10

times increase karta hai.

Mathematically

10 Threads

×

10

=

100

Final answer hona chahiye.

------------------------------------------------------------

English
--------

The program creates

10 threads.

Each thread increments the same variable

10

times.

Expected Result

10 × 10

=

100

====================================================================
Code
====================================================================

import threading

counter = 0

lock = threading.Lock()

====================================================================
counter = 0
====================================================================

counter ek GLOBAL variable hai.

Sabhi threads isi variable ko access karenge.

Memory

Main Process

│

└── counter = 0

Thread1

↓

Uses counter

Thread2

↓

Uses counter

Thread3

↓

Uses counter

...

All threads share the SAME variable.

====================================================================
lock = threading.Lock()
====================================================================

Lock ek synchronization object hai.

Sirf

ONE

thread ko critical code execute
karne deta hai.

Imagine

Bathroom

↓

One Key

↓

One Person enters

↓

Door Locked

↓

Others wait outside

↓

Door Opens

↓

Next Person enters

Exactly same concept.

====================================================================
Function
====================================================================

def increment():

    global counter

Why global?

Because

counter

function ke bahar hai.

Without

global

Python new local variable bana dega.

====================================================================
Loop
====================================================================

for _ in range(10):

Means

Run

10

times.

_

means

We don't care about loop variable.

Same as

for i in range(10)

if "i" is never used.

====================================================================
The Important Line
====================================================================

counter += 1

Looks like ONE operation.

Actually

It is NOT.

Python performs multiple steps.

Step 1

Read counter

Suppose

counter

=

50

------------------------------

Step 2

Calculate

50 + 1

=

51

------------------------------

Step 3

Store

51

back into memory.

So

counter += 1

is actually

Read

↓

Calculate

↓

Write

Three separate operations.

====================================================================
What happens WITHOUT Lock?
====================================================================

Imagine

counter = 50

Thread A

reads

50

------------------------------

Before A writes

Thread B also reads

50

------------------------------

Thread A

adds

1

=

51

writes

51

------------------------------

Thread B

also adds

1

=

51

writes

51

Final value

51

Expected

52

One increment is LOST.

This is called

Race Condition.

====================================================================
Visual Example
====================================================================

Counter = 5

Thread A

↓

Read 5

--------------------

Thread B

↓

Read 5

--------------------

Thread A

↓

Write 6

--------------------

Thread B

↓

Write 6

Final

6

Correct Answer

7

One update disappeared.

====================================================================
Why?
====================================================================

Both threads

raced

to update

the same variable.

Whoever writes last

wins.

The earlier update gets overwritten.

====================================================================
With Lock
====================================================================

with lock:

    counter += 1

Means

Acquire Lock

↓

Only ONE thread enters

↓

Increment counter

↓

Release Lock

↓

Next thread enters

Now

No two threads

can modify

counter

at the same time.

====================================================================
Execution with Lock
====================================================================

Counter

=

50

Thread A

↓

Gets Lock

↓

Reads

50

↓

Writes

51

↓

Releases Lock

-----------------------

Thread B

↓

Gets Lock

↓

Reads

51

↓

Writes

52

↓

Releases Lock

Correct Answer

52

No updates lost.

====================================================================
Expected Output
====================================================================

Without Lock

Sometimes

997842

Sometimes

998523

Sometimes

999011

Sometimes

999765

Every run can produce
a different result.

------------------------------------------------------------

With Lock

Always

100

====================================================================
Why is Lock Slower?
====================================================================

Without Lock

All threads

try to execute immediately.

Fast

But Wrong.

------------------------------------------------------------

With Lock

Only one thread

can execute

the critical section.

Slightly slower

But Correct.

Correctness is more important.

====================================================================
What is Critical Section?
====================================================================

Critical Section

means

A piece of code

that modifies

shared data.

Example

counter += 1

Database Update

Account Balance

Inventory Count

Wallet Amount

Bank Transaction

These should always
be protected.

====================================================================
Real World Examples
====================================================================

Bank Account

Thread1

Withdraw ₹100

--------------------

Thread2

Withdraw ₹200

Without Lock

Balance becomes incorrect.

------------------------------------------------------------

Online Shopping

Two users buy

Last Phone

Without Lock

Both orders succeed.

Inventory becomes

-1

------------------------------------------------------------

Hospital

Two nurses update

same patient record.

Without Lock

One update disappears.

====================================================================
JavaScript Comparison
====================================================================

JavaScript

normally

doesn't have this problem
on the main thread

because JavaScript

runs one statement

at a time.

But

Worker Threads

or

multiple servers

can have similar
shared-state issues.

Python Threads

share memory,

so race conditions
are common.

====================================================================
Best Practice
====================================================================

Protect only

the minimum code

inside

with lock:

Bad

with lock:

    Download File

    Read Image

    Send Email

Too much work.

------------------------------------------------------------

Good

Download

↓

Process

↓

with lock:

    counter += 1

Only protect
shared resources.

====================================================================
Golden Rule
====================================================================

Reading Shared Data

↓

Usually Safe

----------------------------

Writing Shared Data

↓

Use Lock

----------------------------

Shared Variable

+

Multiple Threads

↓

Always Think About

Race Condition

====================================================================
End of Notes
====================================================================

"""