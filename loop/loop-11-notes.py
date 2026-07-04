# ==========================================
# Walrus Operator with while Loop
# ==========================================

# := assigns a value and immediately
# uses it in the condition.

# Example

while (name := input("Name: ")) not in users:
    print("Invalid User")

# Equivalent Code

name = input("Name: ")

while name not in users:
    print("Invalid User")
    name = input("Name: ")

# capitalize()

# Converts:
# rinkesh -> Rinkesh

# Used because string comparison
# is case-sensitive.

# Rule to Remember

# :=

# Assign

# +

# Use Immediately

# not in

# Means the value does not exist
# in the list.