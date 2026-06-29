"""
List Methods: append() and remove()

append(item):
- Adds a new item at the end of the list.
- Modifies the original list.
- Returns nothing (None).

Example:
users = ["Rinkesh", "Nitish"]
users.append("Chunnu")
# ['Rinkesh', 'Nitish', 'Chunnu']

remove(value):
- Removes the first occurrence of the specified value.
- Removes by value, not by index.
- Raises ValueError if the value is not found.

Example:
users.remove("Nitish")
# ['Rinkesh', 'Chunnu']

Difference:
append() -> Adds an item to the end.
remove() -> Deletes an item by its value.
pop() -> Deletes an item by its index.
"""