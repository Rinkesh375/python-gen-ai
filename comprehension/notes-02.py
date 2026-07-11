"""
==========================================================
Topic: Set Comprehension
==========================================================

Code
----

recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elachi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

data = {
    item
    for value in recipes.values()
    for item in value
}

print(data)

==========================================================
What is Happening?
==========================================================

recipes is a dictionary.

Dictionary

{
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elachi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"]
}

Each key is a tea name.

Each value is a list of ingredients.

==========================================================
Step 1
==========================================================

recipes.values()

returns

[
    ["ginger", "cardamom", "clove"],
    ["cardamom", "milk"],
    ["ginger", "black pepper", "clove"]
]

Notice:

Only the VALUES are returned.

The dictionary keys are ignored.

==========================================================
Step 2
==========================================================

for value in recipes.values()

Python loops over each list.

Iteration 1

value

["ginger", "cardamom", "clove"]

------------------------------------------

Iteration 2

value

["cardamom", "milk"]

------------------------------------------

Iteration 3

value

["ginger", "black pepper", "clove"]

==========================================================
Step 3
==========================================================

for item in value

Now Python loops through each ingredient
inside the current list.

Example

value

["ginger", "cardamom", "clove"]

Iteration

item = "ginger"

item = "cardamom"

item = "clove"

Then Python moves to the next list.

==========================================================
Internal Working
==========================================================

Python is actually doing this:

data = set()

for value in recipes.values():

    for item in value:

        data.add(item)

==========================================================
Complete Execution
==========================================================

Start

data = {}

------------------------------------------

First List

["ginger", "cardamom", "clove"]

Add

ginger

data

{"ginger"}

----------------

Add

cardamom

data

{"ginger", "cardamom"}

----------------

Add

clove

data

{"ginger", "cardamom", "clove"}

==========================================================

Second List

["cardamom", "milk"]

Add

cardamom

Already exists.

Sets do NOT allow duplicates.

Nothing changes.

----------------

Add

milk

data

{
    "ginger",
    "cardamom",
    "clove",
    "milk"
}

==========================================================

Third List

["ginger", "black pepper", "clove"]

Add

ginger

Already exists.

Ignored.

----------------

Add

black pepper

Added.

----------------

Add

clove

Already exists.

Ignored.

==========================================================
Final Output
==========================================================

{
    'ginger',
    'cardamom',
    'clove',
    'milk',
    'black pepper'
}

The order may be different because
SETS are unordered.

==========================================================
Why Use a Set Here?
==========================================================

The ingredients contain duplicates.

Example

ginger appears twice.

cardamom appears twice.

clove appears twice.

A set automatically removes duplicates.

Result

Only UNIQUE ingredients remain.

==========================================================
Difference Between List and Set
==========================================================

List

[]

✔ Ordered
✔ Allows duplicates

Example

["A", "A", "B"]

------------------------------------------

Set

{}

✔ Unordered
✔ No duplicates

Example

{"A", "B"}

==========================================================
Easy Formula
==========================================================

Set Comprehension

{
    expression
    for item in iterable
}

Nested Set Comprehension

{
    item
    for outer in iterable
    for item in outer
}

==========================================================
Real-World Example
==========================================================

Imagine three tea recipes.

Masala Chai

ginger
cardamom
clove

------------------

Elachi Chai

cardamom
milk

------------------

Spicy Chai

ginger
black pepper
clove

You want a shopping list.

Instead of buying:

ginger
cardamom
clove
cardamom
milk
ginger
black pepper
clove

You only need:

ginger
cardamom
clove
milk
black pepper

A set automatically creates this unique shopping list.

==========================================================
Golden Rule
==========================================================

Use []  → List Comprehension

Use {}  → Set Comprehension

List keeps duplicates.

Set removes duplicates automatically.

==========================================================
"""