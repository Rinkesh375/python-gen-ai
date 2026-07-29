"""
==========================================================
Topic: Dictionary Unpacking (**)
==========================================================

===========================
1. Hinglish Explanation
===========================

Code:

print(**{"id":1, "name":"Rinkesh", "Married":False})

** kya hai?

** (double asterisk) ko Dictionary Unpacking ya Keyword
Argument Unpacking bolte hain.

Ye dictionary ke saare key-value pairs ko alag-alag
keyword arguments me convert kar deta hai.

Step-by-Step

Dictionary:

{
    "id": 1,
    "name": "Rinkesh",
    "Married": False
}

Python internally isse convert karta hai:

print(id=1, name="Rinkesh", Married=False)

Ab problem ye hai ki print() function ke paas
id, name aur Married naam ke parameters hote hi nahi hain.

print() sirf ye keyword arguments accept karta hai:

- sep
- end
- file
- flush

Isliye Python TypeError throw karta hai.

Output

TypeError:
'id' is an invalid keyword argument for print()

--------------------------------------------
Correct Example
--------------------------------------------

def show(id, name, Married):
    print(id)
    print(name)
    print(Married)

person = {
    "id": 1,
    "name": "Rinkesh",
    "Married": False
}

show(**person)

Python internally:

show(id=1, name="Rinkesh", Married=False)

Output

1
Rinkesh
False

Real Life

API se data dictionary me aata hai.

Us dictionary ko directly function me pass kar sakte ho
using **.

==========================================================

===========================
2. English Explanation
===========================

Code:

print(**{"id":1, "name":"Rinkesh", "Married":False})

What is ** ?

The ** (double asterisk) operator is called
Dictionary Unpacking or Keyword Argument Unpacking.

It converts every key-value pair of a dictionary into
keyword arguments.

Step-by-Step

Dictionary:

{
    "id": 1,
    "name": "Rinkesh",
    "Married": False
}

Python internally converts it to:

print(id=1, name="Rinkesh", Married=False)

The problem is that print() does not have parameters
named id, name, or Married.

It only accepts these keyword arguments:

- sep
- end
- file
- flush

Therefore Python raises a TypeError.

Output

TypeError:
'id' is an invalid keyword argument for print()

--------------------------------------------
Correct Example
--------------------------------------------

def show(id, name, Married):
    print(id)
    print(name)
    print(Married)

person = {
    "id": 1,
    "name": "Rinkesh",
    "Married": False
}

show(**person)

Python internally converts it to:

show(id=1, name="Rinkesh", Married=False)

Output

1
Rinkesh
False

Real-World Use

API responses, database records, Django, Flask,
FastAPI, and Pydantic frequently use ** to pass
dictionary data into functions.

==========================================================
"""