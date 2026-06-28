"""
// (Floor Division Operator)

Definition:
- Divides two numbers and returns the floor (largest integer less than or equal to the result).

Difference:
/  -> Normal Division (returns decimal/float)
// -> Floor Division (returns floored value)

Examples:
10 / 3  -> 3.3333333333
10 // 3 -> 3

25 // 4 -> 6
9.5 // 2 -> 4.0

Negative Numbers:
-10 // 3 -> -4
Reason:
Python always applies floor(), so it rounds down to the next smaller integer.

Common Uses:
- Counting complete pages
- Finding complete groups
- Converting minutes to hours
- Calculating how many full items fit into a container

Remember:
"/"  = Exact Division
"//" = Floor Division
"""

"---------------------------------------------------------------------------------------------------------------------------"

"""
Underscores (_) in Numbers

- Used to improve readability of large numbers.
- Python ignores underscores while interpreting the value.
- They do NOT change the number.

Example:
million = 1_000_000
billion = 1_000_000_000

Both are equivalent:
1_000_000 == 1000000   # True

Best Practice:
Use underscores when writing large numbers to make code easier to read.
"""