# ==========================================
# enumerate() Notes
# ==========================================

# enumerate() adds an index to each item
# in an iterable.

# Syntax
#
# enumerate(iterable)
#
# enumerate(iterable, start=1)

# Default index starts from 0.

# start parameter changes the starting index.

# Example

months = ["Jan","Feb","Mar"]

print(list(enumerate(months)))

# Output
# [(0,'Jan'), (1,'Feb'), (2,'Mar')]

print(list(enumerate(months, start=1)))

# Output
# [(1,'Jan'), (2,'Feb'), (3,'Mar')]

# Best Practice

# Instead of

# i = 0
# for item in list:
#     print(i,item)
#     i += 1

# Use

# for index, item in enumerate(list):
#     print(index, item)

# Rule to Remember

# enumerate() = Index + Value