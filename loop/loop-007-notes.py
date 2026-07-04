# ==========================================
# Python Scope in Loops
# ==========================================

# A for loop DOES NOT create a new scope.

# The loop variable belongs to the
# current scope.

# After the loop ends,
# the variable still exists.

# It contains the LAST assigned value.

# Example

for x in [1,2,3]:
    pass

print(x)

# Output
# 3

# If break occurs,
# the variable keeps the value where
# break happened.

# Example

for x in [1,2,3]:

    if x == 2:
        break

print(x)

# Output
# 2

# If the loop never executes,
# the variable is never created.

# Example

for x in []:
    pass

print(x)

# NameError

# Python creates new scopes only for:
# ✔ Functions
# ✔ Classes
# ✔ Modules

# Loops and if-statements DO NOT
# create a new scope.