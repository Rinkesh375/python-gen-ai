"""
extend() Method in Python

Definition:
- extend() adds all elements from another iterable (list, tuple, set, string, etc.)
  to the end of the current list.
- It modifies the original list.

Syntax:
list.extend(iterable)

Example:
users = ["Rinkesh", "Nitish"]

users.extend(["Vimal", "Mukesh"])

print(users)

Output:
['Rinkesh', 'Nitish', 'Vimal', 'Mukesh']

append() vs extend()

append():
- Adds one item to the end.
- If a list is passed, the entire list becomes a single element.

Example:
users.append(["A", "B"])

Output:
['Rinkesh', 'Nitish', ['A', 'B']]

extend():
- Adds each element of the iterable separately.

Example:
users.extend(["A", "B"])

Output:
['Rinkesh', 'Nitish', 'A', 'B']

Key Points:
- extend() modifies the original list.
- Works with lists, tuples, sets, strings, and other iterables.
- Used when you want to merge or combine multiple collections into one list.
"""