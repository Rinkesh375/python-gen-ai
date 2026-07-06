# ============================================================
# Topic: Default Mutable Arguments
# ============================================================

# Default parameter values are evaluated only ONCE,
# when the function is defined (not every time it is called).

def test(users=[]):
    users.append("Rinkesh")
    print(users)

test()
test()

# Output:
# ['Rinkesh']
# ['Rinkesh', 'Rinkesh']


# ------------------------------------------------------------
# Why?
# ------------------------------------------------------------

# The default list is created only once.
# Every function call without an argument uses
# the SAME list object.

# Function
#    │
#    ▼
# Default List
# []

# After first call
# ["Rinkesh"]

# After second call
# ["Rinkesh", "Rinkesh"]


# ------------------------------------------------------------
# Mutable Default Arguments
# ------------------------------------------------------------

# Avoid using mutable objects as default values.

# Bad
def bad(users=[]):
    pass

# Mutable Objects:
# ✔ List
# ✔ Dictionary
# ✔ Set


# ------------------------------------------------------------
# Recommended Way
# ------------------------------------------------------------

def good(users=None):
    if users is None:
        users = []

    users.append("Rinkesh")
    print(users)

good()
good()

# Output:
# ['Rinkesh']
# ['Rinkesh']


# ------------------------------------------------------------
# Interview Notes
# ------------------------------------------------------------

# Q. Why does the list keep growing?
# Ans: Because the default list is created only once
# and reused for every function call.

# Q. What is the recommended practice?
# Ans: Use None as the default value and create
# a new list inside the function.

# Q. Are mutable default arguments recommended?
# Ans: No.


# ------------------------------------------------------------
# Quick Revision
# ------------------------------------------------------------

# ✔ Default arguments are evaluated only once.
# ✔ Lists are mutable.
# ✔ The same default list is reused.
# ✔ Modifying it affects future function calls.
# ✔ Use None instead of [] as a default parameter.




















# ============================================================
# Topic: Passing Your Own Argument vs Default Argument
# ============================================================

# If an argument is provided, Python ignores the default value.
# The passed argument is used instead.

def test(users=[]):
    users.append("Rinkesh")
    print(users)

test()        # Uses default list
test([1])     # Uses passed list

# Output:
# ['Rinkesh']
# [1, 'Rinkesh']


# ------------------------------------------------------------
# How Python Works
# ------------------------------------------------------------

# test()
# No argument is passed.
# Python uses the default list.

# test([1])
# A list is passed.
# Python uses the passed list and ignores the default list.


# ------------------------------------------------------------
# Memory Example
# ------------------------------------------------------------

# Default List
# ["Rinkesh"]

# Passed List
# [1]

# These are two different list objects.

# Modifying the passed list does NOT modify the default list.


# ------------------------------------------------------------
# Interview Notes
# ------------------------------------------------------------

# Q. When is the default parameter used?
# Ans: Only when no argument is passed.

# Q. What happens if an argument is passed?
# Ans: Python ignores the default value and uses the passed argument.

# Q. Does passing a new list modify the default list?
# Ans: No.


# ------------------------------------------------------------
# Quick Revision
# ------------------------------------------------------------

# ✔ Default value is used only when an argument is omitted.
# ✔ Passing an argument overrides the default value.
# ✔ The passed list and default list are different objects.
# ✔ Changes to the passed list do not affect the default list.