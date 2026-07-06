# ============================================================
# Topic: Passing List to a Function (Mutable Objects)
# ============================================================

# A list is a Mutable object.
# Mutable means its contents can be changed after creation.

users = ["Rinkesh", "Shiv", "Nitish"]


# ------------------------------------------------------------
# Passing a List to a Function
# ------------------------------------------------------------

# When a list is passed to a function,
# Python passes a reference to the same list.

def print_users(userList):
    print(userList)


# ------------------------------------------------------------
# Modifying the List
# ------------------------------------------------------------

# Changing an element of the list changes the original list.

users = ["Rinkesh", "Shiv", "Nitish"]

def print_users(userList):
    userList[0] = "Rinkesh Kumar"

print_users(users)

print(users)

# Output:
# ['Rinkesh Kumar', 'Shiv', 'Nitish']


# ------------------------------------------------------------
# Why?
# ------------------------------------------------------------

# Both variables point to the same list object.

# users
#   │
#   ▼
# ["Rinkesh", "Shiv", "Nitish"]
#   ▲
#   │
# userList

# Changing the list through one variable
# is visible through the other variable.


# ------------------------------------------------------------
# Mutable vs Immutable
# ------------------------------------------------------------

# List  -> Mutable  -> Original object can change.
# String -> Immutable -> Original object cannot change.
# Tuple -> Immutable
# Dictionary -> Mutable
# Set -> Mutable


# ------------------------------------------------------------
# Interview Notes
# ------------------------------------------------------------

# Q. Does modifying a list inside a function affect the original list?
# Ans: Yes.

# Q. Why?
# Ans: Because Python passes a reference to the same mutable object.

# Q. Are lists mutable?
# Ans: Yes.

# Q. Are strings mutable?
# Ans: No.


# ------------------------------------------------------------
# Quick Revision
# ------------------------------------------------------------

# ✔ List is Mutable.
# ✔ Functions receive a reference to the same list.
# ✔ Changing list elements affects the original list.
# ✔ No new list is created unless you explicitly copy it.
# ✔ Strings behave differently because they are Immutable.