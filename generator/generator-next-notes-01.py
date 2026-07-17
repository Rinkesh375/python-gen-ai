"""
==========================================================
Topic: Generators and the yield Keyword
==========================================================

Code
----

def print_alphabets():
    yield "A"
    yield "B"
    yield "C"
    yield "D"
    yield "E"
    yield "F"
    yield "G"

alphabets = print_alphabets()

print(next(alphabets))

==========================================================
What is a Generator?
==========================================================

A Generator is a special type of function that returns
one value at a time instead of returning all values at once.

A normal function uses:

return

A generator function uses:

yield

==========================================================
What is 'yield'?
==========================================================

'yield' pauses the function and returns one value.

When the next value is requested, the function
continues from where it stopped.

Think of it like pressing the "Pause" button
on a video.

Next time you press Play, the video continues
from the same position.

==========================================================
Generator Function
==========================================================

def print_alphabets():
    yield "A"
    yield "B"
    yield "C"
    ...

As soon as Python sees the keyword 'yield',

it automatically treats the function as
a Generator Function.

==========================================================
Creating the Generator
==========================================================

alphabets = print_alphabets()

Nothing is printed.

Nothing is executed.

Python only creates a Generator Object.

Memory

alphabets

↓

<generator object>

==========================================================
Why Doesn't the Function Run Immediately?
==========================================================

Generators use Lazy Execution.

Lazy means:

"Do the work only when someone asks."

Python waits until:

next()

or

for loop

asks for the next value.

==========================================================
Execution Using next()
==========================================================

print(next(alphabets))

Python starts the function.

yield "A"

↓

Returns

"A"

↓

Function pauses here.

Output

A

==========================================================
Internal Execution
==========================================================

Step 1

Call

next(alphabets)

↓

Function starts.

yield "A"

↓

Return "A"

↓

Pause.

----------------------------------------------------------

Step 2

Call

next(alphabets)

↓

Resume after

yield "A"

↓

yield "B"

↓

Return "B"

↓

Pause.

----------------------------------------------------------

Step 3

Call

next(alphabets)

↓

Resume after

yield "B"

↓

yield "C"

↓

Return "C"

↓

Pause.

This continues until all values are yielded.

==========================================================
Using a for Loop
==========================================================

for ch in alphabets:
    print(ch)

Python automatically calls:

next(alphabets)

again and again until the generator finishes.

Output

A
B
C
D
E
F
G

==========================================================
What Happens After the Last yield?
==========================================================

After

yield "G"

there are no more values.

Calling

next(alphabets)

again will raise

StopIteration

Example

next(alphabets)

↓

StopIteration

This tells Python that the generator
has finished producing values.

==========================================================
Generator Flow
==========================================================

Generator Created

↓

next()

↓

yield "A"

↓

Pause

↓

next()

↓

yield "B"

↓

Pause

↓

next()

↓

yield "C"

↓

Pause

↓

...

↓

yield "G"

↓

Pause

↓

next()

↓

StopIteration

==========================================================
Generator vs Normal Function
==========================================================

Normal Function

✔ Uses return
✔ Returns all data at once
✔ Function ends immediately

Example

def demo():
    return 10

----------------------------------------------------------

Generator Function

✔ Uses yield
✔ Returns one value at a time
✔ Function pauses after each yield
✔ Resumes when next() is called

Example

def demo():
    yield 10

==========================================================
Real-World Example
==========================================================

Imagine a vending machine.

It does NOT give all snacks at once.

You press the button.

↓

One snack comes out.

Press again.

↓

Another snack comes out.

The machine remembers where it stopped.

Generators work the same way.

==========================================================
When Should You Use Generators?
==========================================================

Use generators when:

✔ Working with large data.
✔ Reading huge files.
✔ Processing data one item at a time.
✔ Saving memory.

Instead of storing everything in memory,
a generator produces values only when needed.

==========================================================
Golden Rule
==========================================================

return

↓

Ends the function immediately.

------------------------------------------

yield

↓

Returns one value.

Pauses the function.

Continues from the same place
when next() is called.

==========================================================
Quick Revision
==========================================================

✔ Generator functions use yield.

✔ Calling a generator function does NOT execute it.

✔ It returns a Generator Object.

✔ next() starts or resumes the generator.

✔ yield pauses the function.

✔ for loop automatically calls next().

✔ After the last value, Python raises StopIteration.

==========================================================
Interview Questions
==========================================================

Q1. What is a Generator?

Answer:

A generator is a special function that produces
values one at a time using the 'yield' keyword.

----------------------------------------------------------

Q2. What is the difference between
return and yield?

return

• Returns one value.
• Ends the function.

yield

• Returns one value.
• Pauses the function.
• Continues from the same place later.

----------------------------------------------------------

Q3. Why are generators memory efficient?

Answer:

Generators do not store all values in memory.

They generate values only when requested,
making them suitable for large datasets.

==========================================================
"""