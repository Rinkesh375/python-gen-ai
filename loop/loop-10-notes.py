# ==========================================
# Walrus Operator (:=) Notes
# ==========================================

# Introduced in Python 3.8.

# := assigns a value and returns it
# in the same expression.

# Syntax

# if (variable := expression):
#     ...

# Example

value = 23

if (remainder := value % 5):
    print("Not Divisible")

# Equivalent Code

remainder = value % 5

if remainder:
    print("Not Divisible")

# Important

# =  -> Assignment statement

# == -> Comparison operator

# := -> Assignment expression (Walrus)

# Rule to Remember

# := means
# "Assign and Use Immediately."