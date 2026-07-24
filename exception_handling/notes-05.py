"""
==========================================================
.title() Method in Python
==========================================================

What is .title()?

Hinglish
---------
.title() string ke har word ka pehla letter
Capital aur baaki letters small kar deta hai.

English
--------
The .title() method converts the first letter
of every word to uppercase and the remaining
letters to lowercase.

Syntax
------
string.title()

Example 1
---------

tea = "masala chai"

print(tea.title())

Output
------
Masala Chai

Example 2
---------

name = "rInKeSh KuMaR"

print(name.title())

Output
------
Rinkesh Kumar

Difference
----------

.capitalize()

Input
-----
"masala chai"

Output
------
Masala chai

Only first character of the entire string
is capitalized.

------------------------------------------

.title()

Input
-----
"masala chai"

Output
------
Masala Chai

First character of every word
is capitalized.

Common Uses
-----------

✔ Display names
✔ Product names
✔ City names
✔ User-friendly output
✔ Reports and invoices

Remember
--------

.title() returns a NEW string.

It does NOT change the original string.

Example
-------

name = "rinkesh"

new_name = name.title()

print(name)

Output
------
rinkesh

print(new_name)

Output
------
Rinkesh
"""