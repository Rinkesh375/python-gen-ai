"""
====================================================================
        Multiprocessing Queue in Python
====================================================================

Author : Your Python Learning Notes

====================================================================
What is a Queue?
====================================================================

Hinglish
---------

Queue ek communication channel hai.

Iska use

ek process

se

dusre process

tak data bhejne ke liye hota hai.

Queue

FIFO

(FIRST IN FIRST OUT)

principle follow karti hai.

Jo data pehle jayega,

wo pehle bahar niklega.

------------------------------------------------------------

English
--------

A Queue is a communication channel
used between processes.

It safely transfers data
from one process
to another process.

Queue follows

FIFO

(First In First Out).

====================================================================
Real Life Example
====================================================================

Imagine

Restaurant

Customer

↓

Places Order

↓

Queue

↓

Chef

↓

Prepares Food

↓

Queue

↓

Waiter

↓

Customer

Nobody talks directly.

Queue is the messenger.

Exactly the same happens
between processes.

====================================================================
Your Code
====================================================================

from multiprocessing import Process, Queue

====================================================================
Import
====================================================================

Process

Creates a new process.

------------------------------------------------------------

Queue

Creates a shared communication channel
between processes.

Without Queue

Process A

×

Cannot directly access

Process B variables.

====================================================================
Function
====================================================================

def prepare_chai(queue):

Notice

queue

is received as a parameter.

That means

the child process

gets access

to the same Queue object.

====================================================================
queue.put()
====================================================================

queue.put(

    "Masala chai is ready"

)

Meaning

Put data

inside the Queue.

Think

Queue

↓

["Masala chai is ready"]

Queue now stores

one message.

====================================================================
Main Program
====================================================================

if __name__ == "__main__":

Always required
when using multiprocessing.

====================================================================
queue = Queue()
====================================================================

Creates an empty Queue.

Initially

Queue

↓

[ ]

Empty.

====================================================================
Create Process
====================================================================

p = Process(

    target=prepare_chai,

    args=(queue,)

)

Notice

args=(queue,)

The Queue object

is passed

to the child process.

Both processes

can now communicate
through this Queue.

====================================================================
Start Process
====================================================================

p.start()

Child Process starts.

Inside Child Process

prepare_chai(queue)

↓

queue.put("Masala chai is ready")

Queue becomes

[

"Masala chai is ready"

]

====================================================================
join()
====================================================================

p.join()

Main Process waits

until Child Process finishes.

====================================================================
queue.get()
====================================================================

print(

    queue.get()

)

queue.get()

removes

the first item

from the Queue.

Output

Masala chai is ready

Queue becomes empty again.

====================================================================
Execution Flow
====================================================================

Main Process

↓

Create Queue

↓

Create Process

↓

Start Process

↓

Child Process

↓

queue.put()

↓

Message stored

↓

Child Ends

↓

join()

↓

Main Process

↓

queue.get()

↓

Print Message

====================================================================
Visual Diagram
====================================================================

Main Process

        │

        ▼

    Queue

        ▲

        │

Child Process

Child

↓

queue.put()

↓

Queue

↓

queue.get()

↓

Main

====================================================================
FIFO Example
====================================================================

queue.put("Tea")

queue.put("Coffee")

queue.put("Milk")

Queue

↓

["Tea", "Coffee", "Milk"]

queue.get()

↓

Tea

queue.get()

↓

Coffee

queue.get()

↓

Milk

Exactly

First In

↓

First Out

====================================================================
Why can't we use a normal variable?
====================================================================

Suppose

counter = 0

Main Process

↓

Creates Child Process

Child Process

counter = 10

Main Process

counter ?

Still

0

Because

Every process

has its own memory.

Changes

are NOT shared.

====================================================================
Real World Example 1
====================================================================

Image Processing

Main Process

↓

Creates

100 image tasks

↓

Queue

↓

Worker Processes

↓

Each process

takes

one image

from Queue

↓

Processes it

↓

Saves Result

====================================================================
Real World Example 2
====================================================================

PDF Processing

Queue

↓

invoice1.pdf

invoice2.pdf

invoice3.pdf

↓

Worker 1

takes invoice1

↓

Worker 2

takes invoice2

↓

Worker 3

takes invoice3

All work simultaneously.

====================================================================
Real World Example 3
====================================================================

Your Pharma Project

Suppose

You have

100 CSV files.

Main Process

↓

Queue

↓

clinical_trial_1.csv

clinical_trial_2.csv

clinical_trial_3.csv

...

↓

Four Worker Processes

↓

Each worker

takes one file

↓

Reads

↓

Validates

↓

Stores in Database

Queue automatically
distributes the work.

====================================================================
JavaScript Comparison
====================================================================

JavaScript

doesn't have

multiprocessing.Queue()

directly.

Closest ideas are

Worker Threads

↓

postMessage()

or

Child Process

↓

IPC (Inter-Process Communication)

Queue is basically

a safe mailbox

between processes.

====================================================================
Golden Rule
====================================================================

Threads

↓

Shared Memory

↓

No Queue needed
(for simple shared variables)

-----------------------------------

Processes

↓

Separate Memory

↓

Need Queue

(or Pipe)

to exchange data.

====================================================================
End of Notes
====================================================================

"""