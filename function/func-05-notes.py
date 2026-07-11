# ============================================================
# Topic: Returning Multiple Values
# ============================================================

# A Python function always returns ONE object.
# When multiple values are returned using commas,
# Python automatically packs them into a tuple.

def multiple_values():
    name = "Rinkesh"
    age = 25
    city = "FBD"
    country = "India"

    return name, age, city, country

user = multiple_values()

print(user)

# Output:
# ('Rinkesh', 25, 'FBD', 'India')


# ------------------------------------------------------------
# What Python Actually Returns
# ------------------------------------------------------------

# Python converts

# return name, age, city, country

# into

# return (name, age, city, country)

# This is a tuple.


# ------------------------------------------------------------
# Data Type
# ------------------------------------------------------------

user = multiple_values()

print(type(user))

# Output:
# <class 'tuple'>


# ------------------------------------------------------------
# Accessing Values
# ------------------------------------------------------------

print(user[0])     # Rinkesh
print(user[1])     # 25
print(user[2])     # FBD
print(user[3])     # India


# ------------------------------------------------------------
# Tuple Unpacking
# ------------------------------------------------------------

name, age, city, country = multiple_values()

print(name)
print(age)

# Output:
# Rinkesh
# 25


# ------------------------------------------------------------
# Interview Notes
# ------------------------------------------------------------

# Q. Can a function return multiple values?
# Ans: Yes, but Python packs them into a tuple.

# Q. What is the return type?
# Ans: Tuple.

# Q. How can you store returned values separately?
# Ans: Using tuple unpacking.


# ------------------------------------------------------------
# Quick Revision
# ------------------------------------------------------------

# ✔ A function returns only ONE object.
# ✔ Multiple returned values are automatically packed into a tuple.
# ✔ Parentheses are optional in the return statement.
# ✔ The returned tuple can be stored in one variable.
# ✔ Or unpacked into multiple variables.