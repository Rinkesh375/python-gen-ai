"""
====================================================================
             raise, try, except and finally in Python
====================================================================

Author : Your Notes
Purpose : Future Reference

====================================================================
Code
====================================================================

def loading_state(state):
    try:
        if isinstance(state, bool):
            print("LOADING..." if state else "NOT LOADING...")
        else:
            raise ValueError(f"{state} is not a boolean value.")

    except ValueError as error:
        print(error)

    finally:
        print("Pass to the next stage.")


====================================================================
What is the purpose of this function?
====================================================================

Hinglish
---------

Ye function check karta hai ki user ne Boolean value
(True ya False) di hai ya nahi.

Agar Boolean hai

to loading status print karega.

Agar Boolean nahi hai

to khud ValueError generate karega.

Us error ko except handle karega.

Aur finally block hamesha chalega.

------------------------------------------------------------

English
---------

This function checks whether the given value
is a Boolean (True or False).

If it is Boolean

it prints the loading state.

Otherwise

it manually raises a ValueError.

The exception is handled inside the except block.

The finally block always executes.

====================================================================
Step 1
====================================================================

def loading_state(state):

Hinglish

Ek function banaya hai.

Ye function ek parameter leta hai.

state

English

A function named loading_state()

takes one argument called state.

====================================================================
Step 2
====================================================================

try:

Hinglish

Is block ke andar jo bhi code hai

agar usme error aayega

to program crash nahi hoga.

Instead

Python except block me chala jayega.

English

The try block contains code that
might generate an exception.

====================================================================
Step 3
====================================================================

isinstance(state, bool)

Hinglish

Ye check karta hai

state Boolean hai ya nahi.

Examples

True

✔

False

✔

1

❌

"Hello"

❌

[]

❌

{}

❌

English

isinstance()

checks whether an object belongs
to a specific datatype.

Syntax

isinstance(object, datatype)

Example

isinstance(True, bool)

Output

True

Example

isinstance(1, bool)

Output

False

====================================================================
Step 4
====================================================================

print("LOADING..." if state else "NOT LOADING...")

Hinglish

Ye Python ka Ternary Operator hai.

Agar

state == True

to

LOADING...

print hoga.

Agar

state == False

to

NOT LOADING...

print hoga.

Ye shortcut hai.

Instead of

if state:
    print("LOADING...")
else:
    print("NOT LOADING...")

English

This is called the Ternary Operator.

It is a one-line if-else statement.

Syntax

value_if_true if condition else value_if_false

====================================================================
Step 5
====================================================================

raise ValueError(...)

Hinglish

Normally Python khud error deta hai.

Lekin

raise

ka use karke hum khud bhi error generate kar sakte hain.

Example

raise ValueError("Age is invalid")

Output

ValueError: Age is invalid

English

The raise keyword is used to
manually create an exception.

====================================================================
Step 6
====================================================================

except ValueError as error:

Hinglish

Agar ValueError aaya

to Python us error ko

error

variable me store karega.

Phir

print(error)

actual message print karega.

English

If a ValueError occurs,

Python stores the exception
inside the variable

error

which can then be printed.

====================================================================
Step 7
====================================================================

finally

Hinglish

finally block

chahe error aaye

ya na aaye

hamesha execute hota hai.

Use Cases

✔ Close File

✔ Close Database

✔ Logout User

✔ Cleanup

English

The finally block always executes

whether an exception occurs or not.

====================================================================
Execution Flow
====================================================================

Example

loading_state(True)

Step 1

True arrives

↓

isinstance(True,bool)

↓

True

↓

Print

LOADING...

↓

finally

↓

Pass to the next stage.

------------------------------------------------------------

loading_state(False)

↓

isinstance(False,bool)

↓

True

↓

NOT LOADING...

↓

finally

↓

Pass to the next stage.

------------------------------------------------------------

loading_state(1)

↓

isinstance(1,bool)

↓

False

↓

raise ValueError

↓

except

↓

1 is not a boolean value.

↓

finally

↓

Pass to the next stage.

====================================================================
Output
====================================================================

loading_state(True)

LOADING...
Pass to the next stage.

------------------------------------------------------------

loading_state(False)

NOT LOADING...
Pass to the next stage.

------------------------------------------------------------

loading_state("Hello")

Hello is not a boolean value.
Pass to the next stage.

====================================================================
Important Interview Points
====================================================================

Q1. Why use raise?

Answer

To manually generate an exception.

------------------------------------------------------------

Q2. Why use isinstance()?

Answer

To check the datatype of an object.

------------------------------------------------------------

Q3. Does finally always execute?

Answer

YES.

Even if an exception occurs.

------------------------------------------------------------

Q4. Why use except ValueError instead of except?

Answer

Because it catches only the required error
and follows Python best practices.

====================================================================
Quick Revision
====================================================================

try
----
Code that may produce an error.

except
-------
Handles the error.

raise
------
Creates an error manually.

finally
---------
Always executes.

isinstance()
------------
Checks datatype.

====================================================================
Golden Rule
====================================================================

✔ Validate input before processing.

✔ Raise meaningful exceptions.

✔ Catch only the exceptions you expect.

✔ Use finally for cleanup code.

====================================================================
End of Notes
====================================================================

"""