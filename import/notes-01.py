"""
==========================================================
Topic: Importing Modules vs Importing Functions
==========================================================

Project Structure
-----------------

project/
│
├── main.py
│
└── recipes/
    │
    ├── __init__.py
    └── flavours.py


flavours.py
-----------

def ginger_chai():
    return "Ginger Chai ☕"

def elachai_chai():
    return "Elachai Chai ☕"

==========================================================
Method 1: Import the Entire Module
==========================================================

Code
----

import recipes.flavours

print(recipes.flavours.elachai_chai())
print(recipes.flavours.ginger_chai())


Hinglish Explanation
--------------------

Yaha hum Python ko bol rahe hain:

    "Pura module import kar do."

Python recipes folder ke andar jayega aur
flavours.py ko import karega.

Ab Python sirf module ko janta hai.

Isliye function call karte time hume
module ka pura path likhna padega.

Example:

recipes.flavours.ginger_chai()

Python internally aise dekhta hai:

recipes
   │
   └── flavours
          │
          ├── ginger_chai()
          └── elachai_chai()

Output
------

Elachai Chai ☕
Ginger Chai ☕

Advantages
----------

✔ Easy to understand
✔ No naming conflicts
✔ Best when using many functions

Disadvantages
-------------

✘ Function call becomes longer.

==========================================================
Method 2: Import Specific Functions
==========================================================

Code
----

from recipes.flavours import elachai_chai, ginger_chai

print(elachai_chai())
print(ginger_chai())


Hinglish Explanation
--------------------

Yaha hum Python se bol rahe hain:

    "Pura module mat lao,
     sirf ye functions le aao."

Python directly ye functions current file me
available kara deta hai.

Ab module ka naam likhne ki zarurat nahi.

Simply likho:

ginger_chai()

instead of

recipes.flavours.ginger_chai()

Python internally:

Current File
│
├── ginger_chai()
└── elachai_chai()

Output
------

Elachai Chai ☕
Ginger Chai ☕

Advantages
----------

✔ Shorter code
✔ Easy when importing only a few functions

Disadvantages
-------------

✘ Name conflicts ho sakte hain agar
  different modules me same function name ho.

==========================================================
Internal Working
==========================================================

Method 1

import recipes.flavours

Memory:

recipes
   │
   └── flavours
          │
          ├── ginger_chai()
          └── elachai_chai()

Access:

recipes.flavours.ginger_chai()


------------------------------------------

Method 2

from recipes.flavours import ginger_chai

Memory:

Current File
│
└── ginger_chai()

Access:

ginger_chai()

==========================================================
Real World Example
==========================================================

Imagine a company.

Company
│
└── HR Department
       │
       ├── hireEmployee()
       └── fireEmployee()


Method 1

You say:

Company.HR.hireEmployee()

You mention the department every time.


Method 2

You say:

Bring only hireEmployee()

Now simply call:

hireEmployee()

==========================================================
Comparison
==========================================================

import recipes.flavours

✔ Imports the entire module
✔ Call using module name
✔ Clear and readable
✔ Avoids naming conflicts

Example:

recipes.flavours.ginger_chai()


------------------------------------------

from recipes.flavours import ginger_chai

✔ Imports only selected functions
✔ Direct function call
✔ Shorter syntax
✔ Can create naming conflicts

Example:

ginger_chai()

==========================================================
When Should You Use Which?
==========================================================

Use import module when:

✔ Using many functions
✔ Want clear code
✔ Avoiding name conflicts

Example:

import math

print(math.sqrt(25))
print(math.pi())


------------------------------------------

Use from module import function when:

✔ Using only a few functions
✔ Want shorter code

Example:

from math import sqrt

print(sqrt(25))

==========================================================
Golden Rule (Easy to Remember)
==========================================================

import module

👉 Bring the whole toolbox.

Use:

module.function()


------------------------------------------

from module import function

👉 Bring only the required tools.

Use:

function()

==========================================================
Summary
==========================================================

import module

• Imports the whole module
• Longer syntax
• More readable
• Safer
• Preferred in large projects


from module import function

• Imports selected functions
• Short syntax
• Cleaner
• Best for small scripts
• Can cause naming conflicts

==========================================================
Interview Question
==========================================================

Q. What is the difference between

import module

and

from module import function ?

Answer:

import module imports the entire module, so
functions are accessed using the module name.

Example:

import math
math.sqrt(25)

Whereas

from module import function

imports only the required function, allowing
it to be called directly.

Example:

from math import sqrt
sqrt(25)

==========================================================

"""