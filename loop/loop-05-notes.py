# ==========================================
# zip() Notes
# ==========================================

# zip() combines two or more iterables
# element by element.

# Syntax

# zip(iterable1, iterable2)

# Returns a zip object.

# Each element becomes a tuple.

# Example

names = ["A","B","C"]

marks = [90,80,70]

print(list(zip(names, marks)))

# Output

# [('A',90), ('B',80), ('C',70)]

# Best Practice

for name, mark in zip(names, marks):
    print(name, mark)

# Important

# zip() stops when the shortest iterable ends.

# If one list has extra elements,
# they are ignored.

# Rule to Remember

# zip() = Pair items from multiple iterables.