"""
insert() Method in Python

Definition:
- insert() adds an element at a specific index in a list.
- Existing elements are shifted one position to the right.
- It modifies the original list.

Syntax:
list.insert(index, value)

Example:
numbers = [1, 2, 4, 5]

numbers.insert(2, 3)

print(numbers)

Output:
[1, 2, 3, 4, 5]

Key Points:
- insert(0, value) -> Inserts at the beginning.
- insert(index, value) -> Inserts at the specified position.
- If the index is larger than the list length, the value is added at the end.
- Existing elements shift to the right after insertion.

Difference:
append(value) -> Adds at the end.
insert(index, value) -> Adds at a specific position.
"""