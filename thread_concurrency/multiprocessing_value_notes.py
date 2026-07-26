"""
====================================================================
            multiprocessing.Value in Python
====================================================================

Author : Your Python Learning Notes

====================================================================
What is Value?
====================================================================

Hinglish
---------

Normally

har process

apni alag memory rakhta hai.

Suppose

Process A

counter = 5

Process B

counter = 10

Ye dono alag memory me hain.

Ek process ke changes

dusre process ko

nahi dikhte.

------------------------------------------------------------

Value()

ek shared memory object banata hai.

Jise

sabhi processes

read aur update

kar sakte hain.

------------------------------------------------------------

English
--------

Normally

every process

has its own memory.

Changes made by one process

are NOT visible

to another process.

Value()

creates

ONE shared variable

that every process

can access.

====================================================================
Import
====================================================================

from multiprocessing import Process, Value

Process

Creates a new process.

-----------------------------

Value

Creates one shared variable
in shared memory.

====================================================================
Function
====================================================================

def increment(counter):

Notice

counter

is passed as an argument.

It is NOT a normal integer.

It is a

Value object.

====================================================================
Loop
====================================================================

for _ in range(100000):

Increase the counter

100000 times.

====================================================================
The Important Line
====================================================================

counter.value += 1

Why

.value ?

Because

counter

is NOT an integer.

It is an object.

Inside that object

the actual integer

is stored in

.value

Think

counter

↓

+------------------+

| Value Object |

| |

| value = 0 |

| |

| lock |

+------------------+

====================================================================
Why not simply write?
====================================================================

counter += 1

Because

counter

is not

0

5

10

It is

Value('i',0)

object.

Correct

counter.value += 1

Wrong

counter += 1

====================================================================
What does this mean?
====================================================================

counter = Value('i',0)

Break it down.

Value(

'i',

0

)

--------------------------------------

'i'

means

signed integer.

Exactly like

int

--------------------------------------

0

means

starting value.

So

Initially

counter.value

=

0

====================================================================
Common Type Codes
====================================================================

'i'

Integer

--------------------------------------

'd'

Double (float)

--------------------------------------

'f'

Float

--------------------------------------

'c'

Character

--------------------------------------

'b'

Signed Char

====================================================================
Shared Memory
====================================================================

Without Value

Process1

counter = 5

--------------------

Process2

counter = 0

Separate Memory

--------------------

Main Process

counter = 0

Nothing is shared.

====================================================================
With Value
====================================================================

Shared Memory

↓

counter.value

↓

0

All processes

read

and

update

the SAME variable.

====================================================================
Lock
====================================================================

with counter.get_lock():

Why?

Because

counter.value += 1

is NOT one operation.

Actually

Python does

Read

↓

Calculate

↓

Write

Exactly like threading.

Without Lock

Process A

reads

50

--------------------

Process B

reads

50

--------------------

Process A

writes

51

--------------------

Process B

writes

51

Expected

52

Actual

51

One update lost.

====================================================================
counter.get_lock()
====================================================================

Every

Value()

already has

its own lock.

You don't create

another Lock().

Instead

you ask

the Value object

for its built-in lock.

counter.get_lock()

↓

Returns Lock

↓

with

uses it

↓

Automatically releases it.

====================================================================
Visual
====================================================================

Shared Memory

counter.value

↓

50

------------------------

Process A

Gets Lock

↓

Updates

↓

51

↓

Releases Lock

------------------------

Process B

Gets Lock

↓

Updates

↓

52

↓

Releases Lock

Correct Answer

====================================================================
Main Program
====================================================================

counter = Value('i',0)

Creates

shared integer

starting at

0

====================================================================
Processes
====================================================================

processes = [

Process(...)

for _ in range(4)

]

Creates

4 processes.

Each process

runs

increment(counter)

====================================================================
Execution
====================================================================

Each process

adds

100000

Total

4

×

100000

=

400000

Expected Output

Final counter value:

400000

====================================================================
Why pass counter?
====================================================================

args=(counter,)

Every process

receives

the SAME

shared Value object.

All processes

work on

one shared counter.

====================================================================
Execution Flow
====================================================================

Main Process

↓

Create Shared Value

↓

counter.value = 0

↓

Create 4 Processes

↓

Process1

↓

Increment

↓

Shared Counter

--------------------

Process2

↓

Increment

↓

Shared Counter

--------------------

Process3

↓

Increment

↓

Shared Counter

--------------------

Process4

↓

Increment

↓

Shared Counter

↓

join()

↓

Print

400000

====================================================================
Real World Example
====================================================================

Suppose

4 worker processes

are importing

CSV files.

Every time

one file finishes

increase

processed_files

by 1.

processed_files

must be shared.

Worker1

↓

processed_files = 10

Worker2

↓

processed_files = 11

Worker3

↓

processed_files = 12

Main Process

can display

Processed

12 Files

====================================================================
Difference Between Queue and Value
====================================================================

Queue

Stores

many messages/tasks.

Example

Task1

Task2

Task3

Task4

------------------------------------------------

Value

Stores

ONE shared value.

Example

counter = 125

progress = 80

is_finished = True

====================================================================
JavaScript Comparison
====================================================================

JavaScript

does not have

multiprocessing.Value()

directly.

Worker Threads

communicate using

postMessage()

or

SharedArrayBuffer

SharedArrayBuffer

is conceptually similar

because multiple workers

can access shared memory.

====================================================================
Golden Rule
====================================================================

Need to share

ONE number

↓

Use

Value()

-------------------------------------

Need to share

Many tasks/messages

↓

Use

Queue()

-------------------------------------

Whenever multiple processes

modify

Value()

↓

Protect it with

get_lock()

====================================================================
End of Notes
====================================================================

"""