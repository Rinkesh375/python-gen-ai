"""
====================================================================
                 Multithreading in Python
====================================================================

Author : Your Notes
Purpose : Future Reference

====================================================================
What is Multithreading?
====================================================================

Hinglish
---------

Normally Python ek time par ek hi task karta hai.

Example

1. Take Order
2. Brew Tea
3. Serve Tea

Ye sab ek ke baad ek hoga.

Lekin

Multithreading ki help se

Python multiple tasks ko ek saath
execute kar sakta hai.

Ye especially useful hai

✔ Downloading Files

✔ API Calls

✔ Reading Files

✔ Sending Emails

✔ Chat Applications

✔ Games

✔ GUI Applications

------------------------------------------------------------

English
---------

Multithreading allows a program
to perform multiple tasks concurrently.

Instead of waiting for one task to finish,

another task can also execute.

====================================================================
Code
====================================================================

import threading
import time

def take_order():
    for i in range(1,5):
        print(f"Taking order no:{i}")
        time.sleep(1)


def brew_order():
    for i in range(1,5):
        print(f"Brew order no:{i}")
        time.sleep(2)


order = threading.Thread(target=take_order)
brewOrder = threading.Thread(target=brew_order)

order.start()
brewOrder.start()

order.join()
brewOrder.join()

====================================================================
Step 1
====================================================================

import threading

Hinglish
---------

Python ka threading module import kiya.

Ye multiple threads banane ke liye use hota hai.

English
--------

Imports Python's threading module.

====================================================================
Step 2
====================================================================

import time

Hinglish
---------

time module use kiya hai

sleep()

function ke liye.

English
--------

Imports the time module.

Used for

time.sleep()

====================================================================
Step 3
====================================================================

def take_order():

Hinglish
---------

Ye function customer ka order leta hai.

Loop

1

↓

4

tak chalega.

Har order ke baad

1 second wait karega.

Example Output

Taking order no:1

(wait 1 sec)

Taking order no:2

English
--------

This function simulates taking customer orders.

====================================================================
Step 4
====================================================================

time.sleep(1)

Hinglish
---------

Program ko

1 second

ke liye pause kar deta hai.

English
--------

Pauses the current thread for one second.

====================================================================
Step 5
====================================================================

def brew_order():

Hinglish
---------

Ye chai banane ka function hai.

Har chai banane me

2 second

lagte hain.

English
--------

This function simulates preparing tea.

Each tea takes 2 seconds.

====================================================================
Step 6
====================================================================

order = threading.Thread(target=take_order)

Hinglish
---------

Ye ek Thread object banata hai.

Important

Thread abhi start nahi hua.

Sirf create hua hai.

English
--------

Creates a Thread object.

The thread has NOT started yet.

====================================================================
What is target?
====================================================================

target

batata hai

Thread ko kaunsa function run karna hai.

Example

threading.Thread(target=take_order)

Means

Run

take_order()

inside this thread.

====================================================================
Step 7
====================================================================

order.start()

Hinglish
---------

Ab thread actually start hota hai.

Python

take_order()

ko execute karna start karta hai.

English
--------

Starts the thread.

====================================================================
Step 8
====================================================================

brewOrder.start()

Hinglish
---------

Dusra thread bhi start ho gaya.

Ab dono functions

ek saath chal sakte hain.

English
--------

Starts the second thread.

Now both functions execute concurrently.

====================================================================
Without Threading
====================================================================

take_order()

↓

Finish

↓

brew_order()

Total Time

4 sec

+

8 sec

=

12 sec

====================================================================
With Threading
====================================================================

Taking Order 1

↓

Brew Order 1

↓

Taking Order 2

↓

Taking Order 3

↓

Brew Order 2

↓

Taking Order 4

↓

Brew Order 3

↓

Brew Order 4

Total Time

Around

8 seconds

instead of

12 seconds.

====================================================================
Step 9
====================================================================

join()

Hinglish
---------

join()

main program ko bolta hai

Wait

jab tak ye thread complete na ho jaye.

English
--------

join()

makes the main program wait
until the thread finishes.

====================================================================
Without join()
====================================================================

Thread Start

↓

Main Program Ends

↓

Thread may still be running.

====================================================================
With join()
====================================================================

Thread Start

↓

Main Program waits

↓

Thread Finished

↓

Program Ends

====================================================================
Output (Approximate)
====================================================================

Taking order no:1

Brew order no:1

Taking order no:2

Taking order no:3

Brew order no:2

Taking order no:4

Brew order no:3

Brew order no:4

Notice

Output order can change.

Because

Threads run independently.

====================================================================
Real Life Example
====================================================================

Restaurant

Without Threads

One worker

↓

Take Order

↓

Cook

↓

Serve

↓

Next Customer

------------------------------------------------------------

With Threads

Worker 1

↓

Take Orders

Worker 2

↓

Cook

Worker 3

↓

Serve

Everything happens simultaneously.

====================================================================
Interview Questions
====================================================================

Q

What is a Thread?

Answer

A thread is the smallest unit
of execution inside a process.

------------------------------------------------------------

Q

Difference between start() and join()?

start()

Starts execution.

join()

Waits until thread completes.

------------------------------------------------------------

Q

Does start() immediately execute the function?

Yes.

It schedules the thread to begin execution.

====================================================================
Quick Revision
====================================================================

threading
---------
Creates threads.

Thread()
--------
Creates thread object.

target
------
Function to execute.

start()
-------
Starts thread.

join()
------
Waits for thread completion.

sleep()
-------
Pauses current thread.

====================================================================
Golden Rule
====================================================================

Create Thread

↓

Start Thread

↓

Join Thread

Always remember

Thread()

does NOT start the thread.

Only

start()

starts it.

====================================================================
End of Notes
====================================================================

"""