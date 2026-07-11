# ============================================================
# Topic: filter()
# ============================================================

# filter() selects elements from an iterable
# based on a condition.

# Syntax:
# filter(function, iterable)


# ------------------------------------------------------------
# Example
# ------------------------------------------------------------

numbers = [1, 12, 4, 65, 41, 25, 35, 78, 45]

odd_numbers = list(filter(lambda number: number % 2, numbers))

print(odd_numbers)

# Output:
# [1, 65, 41, 25, 35, 45]


# ------------------------------------------------------------
# How filter() Works
# ------------------------------------------------------------

# filter() calls the function for every element.

# If function returns True
# -> Keep the element

# If function returns False
# -> Remove the element


# ------------------------------------------------------------
# Lambda Function
# ------------------------------------------------------------

# lambda number: number % 2

# Equivalent to

def is_odd(number):
    return number % 2


# ------------------------------------------------------------
# Why list()?
# ------------------------------------------------------------

# filter() returns a filter object (iterator).

# Convert it into a list using list().

result = filter(lambda x: x > 10, [5, 15, 20])

print(type(result))

# Output:
# <class 'filter'>


# ------------------------------------------------------------
# Common Use Cases
# ------------------------------------------------------------

# ✔ Odd numbers
# ✔ Even numbers
# ✔ Remove empty strings
# ✔ Numbers greater than a value
# ✔ Filter dictionary objects
# ✔ Filter active users
# ✔ Filter products by price


# ------------------------------------------------------------
# Interview Notes
# ------------------------------------------------------------

# Q. What does filter() return?
# Ans: A filter object (iterator).

# Q. How do you get a list?
# Ans: Use list(filter(...))

# Q. What should the function return?
# Ans: A truthy or falsy value.

# Q. Can lambda be used with filter()?
# Ans: Yes.


# ------------------------------------------------------------
# Quick Revision
# ------------------------------------------------------------

# ✔ filter() keeps elements that satisfy a condition.
# ✔ It checks every element one by one.
# ✔ True -> Keep.
# ✔ False -> Remove.
# ✔ Commonly used with lambda.
# ✔ Returns a filter object, not a list.