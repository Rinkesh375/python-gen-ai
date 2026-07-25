"""
===========================================================
              with open() in Python
===========================================================

What is with open()?

Hinglish
---------
with open() file ko automatically close karta hai.

Hume

file.close()

likhne ki zarurat nahi padti.

English
--------
The with statement automatically closes
the file after the block finishes.

-----------------------------------------------------------

Does with handle exceptions?

NO

It only closes the file.

If you want to handle errors,

use

try...except

Example

try:

    with open("notes.txt","w") as file:

        file.write("Hello")

except Exception as error:

    print(error)

-----------------------------------------------------------

Behind the Scenes

with open(...)

is roughly equivalent to

file = open(...)

try:

    ...

finally:

    file.close()

Notice

There is

NO

except block.

-----------------------------------------------------------

Advantages

✔ Automatically closes file

✔ Cleaner code

✔ Prevents memory/resource leaks

✔ Safer than manually calling close()

-----------------------------------------------------------

Remember

with

≠

try

with
----
Automatic resource management
(closes file)

try
----
Handles exceptions

Best Practice

try:

    with open("file.txt","r") as file:

        data = file.read()

except FileNotFoundError:

    print("File not found.")

except PermissionError:

    print("Permission denied.")

except Exception as error:

    print(error)

===========================================================
Golden Rule
===========================================================

Use

with open()

for opening files.

Use

try...except

when you want to handle errors.

Both together are the safest and most professional approach.
===========================================================
"""