"""
=====================================================================
                    TRY - EXCEPT IN PYTHON
=====================================================================

Author : Your Notes
Purpose : Future Reference

=====================================================================
What is try-except?
=====================================================================

Hinglish
---------
Kabhi-kabhi program run hote waqt error aa sakta hai.

Agar hum error handle nahi karte,
to program turant crash ho jata hai.

try-except error ko handle karta hai,
taaki program crash na ho.

English
---------
The try-except block is used to handle runtime errors.

Instead of stopping the program,
Python executes the except block and
continues running the remaining code.

=====================================================================
Example 1 (Your First Code)
=====================================================================

Code

try:
    value = 10 / 0
    print(value)

except:
    print("This value cannot be divided.")

Output

This value cannot be divided.

---------------------------------------------------------------------
Is this Correct?
---------------------------------------------------------------------

YES ✔

It works.

But...

This is NOT considered a good practice.

Why?

Because

except:

catches EVERY error.

Example

ZeroDivisionError

TypeError

NameError

IndexError

KeyError

Everything.

Sometimes you don't want that.

=====================================================================
Why is "except:" bad?
=====================================================================

Suppose

try:
    number = int("Hello")

except:
    print("Something went wrong")

Output

Something went wrong

Question

What actually happened?

Was it

TypeError?

ValueError?

NameError?

You don't know.

This makes debugging difficult.

=====================================================================
Better Way
=====================================================================

try:
    value = 10 / 0
    print(value)

except ZeroDivisionError:
    print("Cannot divide by zero.")

Output

Cannot divide by zero.

Now Python only catches

ZeroDivisionError

Other errors will still be shown.

This is GOOD.

=====================================================================
Example 2 (Your Second Code)
=====================================================================

Code

try:
    value = 20 / 0
    print(value)

except ZeroDivisionError:
    print("Cannot divide by zero.")

Output

Cannot divide by zero.

---------------------------------------------------------------------
Is this Correct?
---------------------------------------------------------------------

YES ✔✔✔

This is the recommended way.

=====================================================================
Can we Improve the Message?
=====================================================================

Instead of

print("Zero ZeroDivisionError occuring can not be divided by a number")

Write

print("Cannot divide a number by zero.")

OR

print("Division by zero is not allowed.")

Reason

Simple

Professional

Easy to understand

=====================================================================
Best Practice
=====================================================================

try:
    value = 20 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")

=====================================================================
Handling Multiple Errors
=====================================================================

try:
    number = int("Hello")
    print(10 / number)

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

=====================================================================
Using "as e"
=====================================================================

Instead of writing your own message,
you can print the actual error.

Example

try:
    value = 20 / 0

except ZeroDivisionError as e:
    print(e)

Output

division by zero

---------------------------------------------------------------------

Another Example

try:
    print(name)

except NameError as e:
    print(e)

Output

name 'name' is not defined

=====================================================================
Generic Exception
=====================================================================

Sometimes you don't know
which error may occur.

Then use

try:
    something()

except Exception as e:
    print(e)

Notice

Exception

NOT

except:

Why?

Because

except Exception

is safer and follows Python best practices.

=====================================================================
Difference
=====================================================================

except:

✔ Catches every error

❌ Bad practice

❌ Difficult to debug

-----------------------------------------------------

except Exception as e:

✔ Catches most runtime errors

✔ Gives actual error message

✔ Professional way

-----------------------------------------------------

except ZeroDivisionError:

✔ Best when you know the error

✔ Recommended

✔ Easy to debug

=====================================================================
Quick Revision
=====================================================================

except:
--------
Avoid whenever possible.

except Exception as e:
-----------------------
Good for general error handling.

except ZeroDivisionError:
--------------------------
Best when you know the exact error.

=====================================================================
Interview Question
=====================================================================

Question

Which is better?

except:

OR

except ZeroDivisionError:

Answer

except ZeroDivisionError

Because it catches only the required error
and makes debugging easier.

=====================================================================
Golden Rule
=====================================================================

Always try to catch
the specific exception.

Avoid writing

except:

unless you have a very good reason.

=====================================================================
End of Notes
=====================================================================


"""