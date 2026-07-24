"""


====================================================================
                 PYTHON COMMON ERRORS (EXCEPTIONS)
====================================================================

Author : Your Notes
Purpose: Future Reference
Language: Hinglish + English

====================================================================
What is an Exception?
====================================================================

Hinglish
---------
Exception ka matlab hota hai Runtime Error.

Program likhte time syntax sahi ho sakti hai,
lekin jab program run hota hai aur koi unexpected
problem aa jati hai, usse Exception kehte hain.

Example:

number = 10
print(number / 0)

Output

ZeroDivisionError

English
--------
An Exception is an error that occurs while the program
is running.

====================================================================
1. IndexError
====================================================================

Definition
----------
Occurs when accessing an invalid index in a list,
tuple or string.

Hinglish
---------
Jab List, Tuple ya String ke andar aisa index use
karte ho jo exist hi nahi karta.

Example

numbers = [10,20,30]

print(numbers[5])

Output

IndexError: list index out of range

Why?

List me sirf

0
1
2

index available hain.

Lekin hum

5

access kar rahe hain.

Correct

print(numbers[len(numbers)-1])

OR

if len(numbers)>5:
    print(numbers[5])

English
--------
Python throws IndexError whenever an index
is outside the valid range.

Future Notes
------------

✔ Works with List
✔ Tuple
✔ String

Remember

Maximum index = len(list)-1

====================================================================
2. KeyError
====================================================================

Definition
----------

Occurs when dictionary key does not exist.

Hinglish
---------

Dictionary ke andar jis key ko access kar rahe ho
wo available hi nahi hai.

Example

student = {
    "name":"Rinkesh",
    "age":27
}

print(student["city"])

Output

KeyError: 'city'

Why?

Dictionary me city key hi nahi hai.

Correct

print(student.get("city"))

OR

print(student.get("city","City Not Found"))

English
--------

Dictionary cannot find the requested key.

Future Notes
------------

✔ Only Dictionary

Avoid

dict["key"]

Prefer

dict.get()

====================================================================
3. ZeroDivisionError
====================================================================

Definition
----------

Occurs when dividing by zero.

Hinglish
---------

Kisi bhi number ko 0 se divide nahi kar sakte.

Example

a = 20
b = 0

print(a/b)

Output

ZeroDivisionError

Why?

Maths rule

20 ÷ 0

possible hi nahi hai.

Correct

if b!=0:
    print(a/b)
else:
    print("Cannot divide by zero")

English
--------

Division by zero is mathematically undefined.

Future Notes
------------

✔ Check denominator first.

====================================================================
4. TypeError
====================================================================

Definition
----------

Occurs when incompatible data types
are used together.

Hinglish
---------

Alag-alag datatype ke beech invalid operation.

Example

age="25"

print(age+5)

Output

TypeError

Why?

String + Integer

allowed nahi hai.

Correct

print(int(age)+5)

Example 2

print("Age : "+25)

Wrong

Correct

print("Age : "+str(25))

English
--------

Python cannot perform an operation
between incompatible data types.

Future Notes
------------

Always check

type(variable)

Common combinations

String + Integer ❌

Integer + Float ✅

String + String ✅

List + List ✅

====================================================================
5. NameError
====================================================================

Definition
----------

Occurs when variable/function is not defined.

Hinglish
---------

Python ko variable mila hi nahi.

Example

print(username)

Output

NameError

Why?

username variable banaya hi nahi.

Correct

username="Rinkesh"

print(username)

English
--------

Python cannot find the variable
or function name.

Future Notes
------------

✔ Define variable first

✔ Check spelling

Example

userName

and

username

are different.

====================================================================
6. ValueError
====================================================================

Definition
----------

Correct datatype
Wrong value

Hinglish
---------

Datatype sahi hai

lekin value galat hai.

Example

number=int("abc")

Output

ValueError

Why?

abc ko integer me convert nahi kar sakte.

Correct

number=int("123")

English
--------

Occurs when a function receives
the correct datatype
but invalid value.

Future Notes
------------

int("10")

✔

int("hello")

❌

====================================================================
7. AttributeError
====================================================================

Definition
----------

Object ke paas wo method hi nahi hai.

Hinglish
---------

Hum aisi function call kar rahe hain
jo object support hi nahi karta.

Example

name="Rinkesh"

name.append("Kumar")

Output

AttributeError

Why?

append()

sirf List me hota hai.

English
--------

Object does not have that attribute
or method.

Future Notes
------------

String

.upper()

.lower()

.replace()

List

.append()

.pop()

.remove()

====================================================================
8. ImportError
====================================================================

Definition
----------

Import failed.

Hinglish
---------

Python module mil gaya
lekin requested object nahi mila.

Example

from math import hello

Output

ImportError

Why?

math module me hello naam ki
function nahi hai.

English
--------

Requested object cannot be imported.

====================================================================
9. ModuleNotFoundError
====================================================================

Definition
----------

Module hi install nahi hai.

Example

import tensorflow

Output

ModuleNotFoundError

Why?

Tensorflow install hi nahi hai.

Correct

pip install tensorflow

English
--------

Python cannot find the module.

====================================================================
10. FileNotFoundError
====================================================================

Definition
----------

Requested file exist hi nahi karti.

Example

open("abc.txt")

Output

FileNotFoundError

Why?

abc.txt folder me nahi hai.

Correct

Check

File Name

Path

Folder

====================================================================
11. IndentationError
====================================================================

Definition
----------

Wrong indentation.

Example

if True:
print("Hello")

Output

IndentationError

Correct

if True:
    print("Hello")

Future Notes
------------

Python indentation-sensitive language hai.

====================================================================
12. SyntaxError
====================================================================

Definition
----------

Python grammar wrong.

Example

if True

print("Hello")

Output

SyntaxError

Correct

if True:
    print("Hello")

====================================================================
13. AssertionError
====================================================================

Definition
----------

assert condition failed.

Example

age=15

assert age>=18

Output

AssertionError

Why?

Condition False hai.

====================================================================
14. RuntimeError
====================================================================

Definition
----------

Runtime me unexpected issue.

Usually advanced topics me aata hai.

====================================================================
15. Exception (Parent Class)
====================================================================

Almost saare errors

Exception

class se inherit karte hain.

Example

try:
    print(10/0)

except Exception as e:
    print(e)

====================================================================
How to Read an Error
====================================================================

Example

TypeError:
can only concatenate str
(not "int") to str

Read like this

1.

Error Name

TypeError

2.

Reason

String + Integer

3.

Go to that line

4.

Fix root cause

====================================================================
Quick Revision Table
====================================================================

IndexError
----------
Invalid Index

KeyError
---------
Dictionary Key Missing

ZeroDivisionError
-----------------
Divide by Zero

TypeError
----------
Wrong Datatype

NameError
----------
Variable Not Defined

ValueError
-----------
Wrong Value

AttributeError
--------------
Method Not Available

ImportError
-----------
Object Cannot Import

ModuleNotFoundError
-------------------
Module Missing

FileNotFoundError
-----------------
File Missing

IndentationError
----------------
Wrong Spaces

SyntaxError
-----------
Wrong Python Grammar

AssertionError
--------------
Assert Failed

RuntimeError
------------
Runtime Problem

====================================================================
Golden Rule
====================================================================

Whenever you get an error

STEP 1

Read the LAST line.

STEP 2

Identify Error Name.

STEP 3

Read the Error Message.

STEP 4

Go to that line.

STEP 5

Understand WHY.

STEP 6

Fix the ROOT CAUSE.

Never hide the error.

Understand it.

====================================================================
End of Notes
====================================================================


"""
