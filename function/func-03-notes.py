# ============================================================
# Topic: Keyword Arguments
# ============================================================

# Keyword Arguments assign values using parameter names.
# Python matches values by the parameter name,
# not by their position.

def user_info(name, city, age, isMarried):
    print(name, city, age, isMarried)

user_info(
    name="Rinkesh",
    age=25,
    city="FBD",
    isMarried=False
)

# Output:
# Rinkesh FBD 25 False


# ------------------------------------------------------------
# How Python Matches
# ------------------------------------------------------------

# Parameter          Value
# -----------------------------
# name        <----  "Rinkesh"
# city        <----  "FBD"
# age         <----  25
# isMarried   <----  False

# Order doesn't matter because parameter names are used.


# ------------------------------------------------------------
# Positional Arguments
# ------------------------------------------------------------

# Values are matched by position.

user_info("Rinkesh", "FBD", 25, False)

# Correct

# Wrong example

user_info("Rinkesh", 25, "FBD", False)

# Here Python thinks

# name = "Rinkesh"
# city = 25
# age = "FBD"
# isMarried = False


# ------------------------------------------------------------
# Keyword Arguments
# ------------------------------------------------------------

# Values are matched by parameter names.

user_info(
    age=25,
    city="FBD",
    name="Rinkesh",
    isMarried=False
)

# Works correctly because names are used.


# ------------------------------------------------------------
# Interview Notes
# ------------------------------------------------------------

# Q. Does the order matter for keyword arguments?
# Ans: No.

# Q. Does the order matter for positional arguments?
# Ans: Yes.

# Q. Which is more readable?
# Ans: Keyword arguments.


# ------------------------------------------------------------
# Quick Revision
# ------------------------------------------------------------

# ✔ Positional Arguments -> Matched by position.
# ✔ Keyword Arguments -> Matched by parameter name.
# ✔ Keyword arguments can be written in any order.
# ✔ Positional arguments must follow the correct order.