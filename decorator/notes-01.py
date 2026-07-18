"""
=========================================
Topic: Decorators
=========================================

What is a Decorator?
--------------------
A decorator is a function that adds extra functionality
to another function without changing its original code.

Syntax
------
def decorator(fn):
    def wrapper():
        # Before
        fn()
        # After
    return wrapper

Example
-------
"""

def outer(fn):

    def inner(value):
        print("Before")
        fn(value)
        print("After")

    return inner


@outer
def printValue(value):
    print(value)


printValue(5)

"""
Output
------
Before
5
After

=========================================
How it Works Internally
=========================================

When Python sees

@outer
def printValue(value):
    print(value)

Python automatically converts it into:

def printValue(value):
    print(value)

printValue = outer(printValue)

Step 1
------
Python creates the original function.

printValue
    │
    ▼
Original Function

Step 2
------
Python calls

outer(printValue)

Here,

fn = Original printValue

Step 3
------
outer() creates the inner() function
and returns it.

return inner

Step 4
------
Now,

printValue = inner

So printValue no longer points to the
original function.

Instead,

printValue
    │
    ▼
inner()
    │
    ▼
Original Function (fn)

Step 5
------
When we call

printValue(5)

Python actually executes

inner(5)

Execution Flow
--------------
printValue(5)
      │
      ▼
inner(5)
      │
      ▼
print("Before")
      │
      ▼
fn(5)      ← Original Function
      │
      ▼
print("After")

=========================================
Notes
=========================================

✔ Decorator receives another function.
✔ Creates a wrapper (inner function).
✔ Returns the wrapper function.
✔ @outer is shorthand for:

    printValue = outer(printValue)

✔ The original function is stored inside
  fn and is called using fn(...).

Remember
--------
Decorator = Wrap another function and
add extra work before or after it runs.
"""