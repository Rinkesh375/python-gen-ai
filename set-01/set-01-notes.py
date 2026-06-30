# Set in Python
# -------------
# A set stores only unique values.
# Duplicate values are automatically removed.
# Sets are unordered (no fixed order).

# Union Operator (|)
# ------------------
# | combines two sets and returns a new set
# containing all unique elements from both sets.

user1 = {"Rinkesh", "Nitish", "Abhishek", "Nitish"}
user2 = {"Abhishek", "ABhishek", "Karn", "Arjun", "Ajay", "Vijay"}

allUsers = user1 | user2

print(allUsers)

# Output (order may vary):
# {'Rinkesh', 'Nitish', 'Abhishek', 'ABhishek',
#  'Karn', 'Arjun', 'Ajay', 'Vijay'}








"-----------------------------------------------------------------------------------"

# Intersection (&) in Sets
# ------------------------
# The & operator returns only the common elements
# that exist in BOTH sets.

user1 = {"Rinkesh", "Nitish", "Abhishek", "Nitish"}
user2 = {"Abhishek", "ABhishek", "Karn", "Arjun", "Ajay", "Vijay", "Rinkesh"}

duplicateUsers = user1 & user2

print(duplicateUsers)

# Output (order may vary):
# {'Rinkesh', 'Abhishek'}

# Remember:
# | -> Union (All unique elements)
# & -> Intersection (Only common elements)
# Sets automatically remove duplicate values.






"---------------------------------------------------------------------------------------"

# Difference (-) in Sets
# ----------------------
# The - operator returns elements that are present
# in the FIRST set but NOT in the SECOND set.

user1 = {"Rinkesh", "Nitish", "Abhishek", "Nitish"}
user2 = {"Abhishek", "ABhishek", "Karn", "Arjun", "Ajay", "Vijay", "Rinkesh"}

print(user1 - user2)

# Output:
# {'Nitish'}

# Remember:
# | -> Union (All unique elements)
# & -> Intersection (Common elements)
# - -> Difference (Only elements in first set, not in second)