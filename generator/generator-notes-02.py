"""
==========================================================
Topic: yield from
==========================================================

What is yield from?
-------------------

yield from is used to delegate work to another generator.

Instead of manually writing a loop to yield every value,
Python automatically yields all values from another
generator or iterable.

==========================================================
Syntax
==========================================================

yield from generator()

==========================================================
Equivalent Code
==========================================================

yield from numbers()

is exactly the same as

for value in numbers():
    yield value

==========================================================
Example
==========================================================

def numbers():
    yield 1
    yield 2
    yield 3


def all_numbers():
    yield 0

    yield from numbers()

    yield 4

Output

0
1
2
3
4

==========================================================
Execution Flow
==========================================================

all_numbers()

↓

yield 0

↓

yield from numbers()

↓

yield 1

↓

yield 2

↓

yield 3

↓

Return to all_numbers()

↓

yield 4

==========================================================
Why Use yield from?
==========================================================

Without yield from

for value in generator():
    yield value

With yield from

yield from generator()

✔ Less code
✔ Easier to read
✔ Cleaner syntax
✔ Delegates to another generator

==========================================================
Golden Rule
==========================================================

yield

↓

Returns ONE value.

------------------------------------------

yield from

↓

Returns ALL values from another generator.

==========================================================
Quick Revision
==========================================================

✔ yield returns one value.

✔ yield from returns every value from another generator.

✔ It replaces:

for value in generator():
    yield value

with a single line.

==========================================================
"""