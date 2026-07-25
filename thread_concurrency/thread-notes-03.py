"""
===========================================================
                args in Python Thread
===========================================================

What is args?

args stands for Arguments.

It tells the thread

"What values should be passed to the function?"

-----------------------------------------------------------

Example

def hello(name):
    print(name)

Thread

thread = threading.Thread(
    target=hello,
    args=("Rinkesh",)
)

When thread.start() executes,

Python internally does

hello("Rinkesh")

-----------------------------------------------------------

One Parameter

args=("Rinkesh",)

Notice the comma.

Without comma

(user)

is NOT a tuple.

With comma

(user,)

becomes a tuple.

-----------------------------------------------------------

Two Parameters

def add(a,b):

Thread

thread = threading.Thread(
    target=add,
    args=(10,20)
)

Internally

add(10,20)

-----------------------------------------------------------

Three Parameters

args=("Rinkesh",28,"Faridabad")

Internally

student("Rinkesh",28,"Faridabad")

-----------------------------------------------------------

Remember

target
-------
Which function to run.

args
-----
What values to pass to that function.

===========================================================
Golden Rule
===========================================================

target = Function

args = Function Arguments

thread.start()

↓

Python automatically calls

Function(*args)

===========================================================
"""