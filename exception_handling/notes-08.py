"""
====================================================================
            Python File Handling Examples
====================================================================

These examples demonstrate different ways of working with files
using try, except, and finally.

Topics Covered

1. Writing a File
2. Reading a File
3. Appending Data
4. File Not Found Error
5. Reading Line by Line
6. Copying File Content
7. Deleting a File
8. Best Practice (with open)

====================================================================
Example 1 : Writing into a File
====================================================================

Hinglish
---------
Agar file exist nahi karti,
to "w" mode automatically new file bana deta hai.

Agar file pehle se exist karti hai,
to uska purana data delete ho jayega.

English
---------
Write mode creates a new file if it does not exist.
If the file already exists,
its old content is overwritten.

"""

try:
    file = open("student.txt", "w")
    file.write("Name : Rinkesh\n")
    file.write("Course : Python\n")
    file.write("City : Faridabad\n")

except Exception as error:
    print(error)

finally:
    file.close()


"""
====================================================================
Example 2 : Reading a File
====================================================================

Hinglish
---------
File ke andar jo data hai
wo read() se read hota hai.

English
---------
read() returns the entire file content.
"""

try:
    file = open("student.txt", "r")

    data = file.read()

    print(data)

except FileNotFoundError:
    print("File not found.")

finally:
    file.close()


"""
====================================================================
Example 3 : Appending Data
====================================================================

Hinglish
---------
"a" mode existing data ko delete nahi karta.

Naya data last me add karta hai.

English
---------
Append mode adds data at the end of the file.
"""

try:

    file = open("student.txt", "a")

    file.write("Country : India\n")

except Exception as error:
    print(error)

finally:
    file.close()


"""
====================================================================
Example 4 : File Not Found
====================================================================

Hinglish
---------
Agar file exist nahi karti
aur hum read mode use kare

to FileNotFoundError aata hai.

English
---------
Reading a missing file raises
FileNotFoundError.
"""

try:

    file = open("unknown.txt", "r")

    print(file.read())

except FileNotFoundError as error:

    print(error)

finally:

    print("Program Finished")


"""
====================================================================
Example 5 : Read Line by Line
====================================================================

Hinglish
---------
Kabhi kabhi puri file nahi
sirf ek line read karni hoti hai.

English
---------
readline() reads one line at a time.
"""

try:

    file = open("student.txt", "r")

    print(file.readline())
    print(file.readline())

except Exception as error:

    print(error)

finally:

    file.close()


"""
====================================================================
Example 6 : Copy File Content
====================================================================

Hinglish
---------
Ek file ka data
dusri file me copy karna.

English
---------
Copy content from one file
to another.
"""

try:

    source = open("student.txt", "r")

    destination = open("backup.txt", "w")

    destination.write(source.read())

except Exception as error:

    print(error)

finally:

    source.close()
    destination.close()


"""
====================================================================
Example 7 : Delete a File
====================================================================

Hinglish
---------
os.remove()

file delete karta hai.

English
---------
os.remove()
deletes a file.
"""

import os

try:

    os.remove("backup.txt")

    print("File deleted.")

except FileNotFoundError:

    print("File already deleted.")

except PermissionError:

    print("Permission denied.")


"""
====================================================================
Example 8 : Modern Python (Recommended)
====================================================================

Hinglish
---------
with open()

automatically file close kar deta hai.

Hume

file.close()

likhne ki zarurat nahi padti.

English
---------
The with statement automatically
closes the file after use.
"""

try:

    with open("notes.txt", "w") as file:

        file.write("Learning Python File Handling")

except Exception as error:

    print(error)


"""
====================================================================
Quick Revision
====================================================================

"r"
----
Read File

"w"
----
Write File
(Overwrite old content)

"a"
----
Append Data

"x"
----
Create New File

read()
------
Read entire file

readline()
----------
Read one line

write()
-------
Write data

close()
-------
Close file

====================================================================
Golden Rule
====================================================================

Old Method

file = open(...)

try:
    ...

finally:
    file.close()

-----------------------------------------------------

Recommended Method

with open(...) as file:
    ...

Python automatically closes the file.

====================================================================
End of Notes
====================================================================


"""