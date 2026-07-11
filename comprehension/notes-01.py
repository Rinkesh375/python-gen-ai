"""
==========================================================
Topic: List Comprehension with Conditions (Filtering Data)
==========================================================

List Comprehension Syntax
-------------------------

new_list = [expression for item in iterable if condition]

Think of it as:

For each item in a list
        ↓
Check the condition
        ↓
If True → Keep it
If False → Skip it

==========================================================
Example 1: Filter Specific Names
==========================================================

Code
----

users = [
    "Rinkesh",
    "Nitish",
    "Abhishek",
    "Pulkit",
    "Manish",
    "Rajesh",
    "Sumit"
]

users2 = [
    tea
    for tea in users
    if tea in ("Rinkesh", "Nitish", "Ma", "Karan")
]

print(users2)


Output
------

['Rinkesh', 'Nitish']

Why?

Python checks every item one by one.

----------------------------------------------------------

Iteration 1

tea = "Rinkesh"

Is "Rinkesh" in

("Rinkesh", "Nitish", "Ma", "Karan") ?

Yes ✔

Keep it.

----------------------------------------------------------

Iteration 2

tea = "Nitish"

Is "Nitish" in

("Rinkesh", "Nitish", "Ma", "Karan") ?

Yes ✔

Keep it.

----------------------------------------------------------

Iteration 3

tea = "Abhishek"

Is "Abhishek" in tuple?

No ❌

Skip it.

----------------------------------------------------------

Iteration 4

tea = "Pulkit"

No ❌

Skip it.

----------------------------------------------------------

Iteration 5

tea = "Manish"

Python checks for EXACT values.

Tuple contains

"Ma"

NOT

"Manish"

So

"Manish" == "Ma"

False ❌

Skip it.

----------------------------------------------------------

Iteration 6

tea = "Rajesh"

No ❌

Skip it.

----------------------------------------------------------

Iteration 7

tea = "Sumit"

No ❌

Skip it.

Final Result

['Rinkesh', 'Nitish']

==========================================================
Important Note
==========================================================

The 'in' operator checks for an EXACT match when used
with a tuple or list.

Example

tea = "Manish"

tea in ("Ma", "Nitish")

↓

False

because

"Manish" != "Ma"

----------------------------------------------------------

If you want to check whether a string STARTS WITH
or CONTAINS another string, use methods like:

startswith()

or

in

Examples

tea.startswith("Ma")

↓

True


"Ma" in tea

↓

True

==========================================================
Common Beginner Mistake
==========================================================

Wrong

if ("Rinkesh" or "Nitish" or "Manish") in tea

Python evaluates

("Rinkesh" or "Nitish" or "Manish")

first.

Result

"Rinkesh"

So Python actually runs

if "Rinkesh" in tea

Only "Rinkesh" matches.

----------------------------------------------------------

Correct

if tea in ("Rinkesh", "Nitish", "Manish")

==========================================================
Example 2: Filtering Dictionary Objects
==========================================================

Code
----

users = [
    {"name":"Rinkesh","age":15},
    {"name":"Nitish","age":24},
    {"name":"Mukesh","age":5},
    {"name":"Manish","age":40},
    {"name":"Tanvir","age":18}
]

eligibleVotes = [
    user
    for user in users
    if user["age"] >= 18
]

print(eligibleVotes)

Output
------

[
    {'name': 'Nitish', 'age': 24},
    {'name': 'Manish', 'age': 40},
    {'name': 'Tanvir', 'age': 18}
]

==========================================================
How Python Executes It
==========================================================

Iteration 1

user

{'name':'Rinkesh','age':15}

15 >= 18

False ❌

Skip

----------------------------------------------------------

Iteration 2

user

{'name':'Nitish','age':24}

24 >= 18

True ✔

Keep

----------------------------------------------------------

Iteration 3

user

{'name':'Mukesh','age':5}

5 >= 18

False ❌

Skip

----------------------------------------------------------

Iteration 4

user

{'name':'Manish','age':40}

40 >= 18

True ✔

Keep

----------------------------------------------------------

Iteration 5

user

{'name':'Tanvir','age':18}

18 >= 18

True ✔

Keep

==========================================================
Final Result
==========================================================

eligibleVotes

↓

[
    {'name':'Nitish','age':24},
    {'name':'Manish','age':40},
    {'name':'Tanvir','age':18}
]

==========================================================
Real-World Example
==========================================================

Imagine you have a list of students.

Student
│
├── Name
├── Age
└── Marks

You want only students who are eligible to vote.

Python checks every student.

Age >= 18 ?

Yes ✔

Keep

No ❌

Skip

==========================================================
Golden Formula
==========================================================

Filter Values

new_list = [
    item
    for item in list
    if condition
]

Python always follows these steps:

1. Take one item.
2. Check the condition.
3. If True → Add it to the new list.
4. If False → Ignore it.
5. Repeat until the list ends.

==========================================================
Quick Revision
==========================================================

✔ List comprehension creates a new list.

✔ 'if' filters data.

✔ 'in' with a tuple/list checks for EXACT matches.

✔ For partial string matching, use:

startswith()

or

substring in string

✔ Dictionary values are accessed using keys.

Example

user["age"]

==========================================================
Interview Questions
==========================================================

Q1. What is List Comprehension?

Answer:

List comprehension is a short and Pythonic way to
create a new list by iterating over an existing iterable.
It can also filter items using an optional 'if' condition.

----------------------------------------------------------

Q2. What does 'in' check?

Answer:

When used with a tuple or list, 'in' checks whether
the value exactly matches one of the elements.

Example

"Manish" in ("Manish", "Nitish")

True

"Manish" in ("Ma", "Nitish")

False

----------------------------------------------------------

Q3. How do you filter dictionaries using
list comprehension?

Answer:

Use the dictionary key inside the condition.

Example

eligible = [
    user
    for user in users
    if user["age"] >= 18
]

==========================================================
"""