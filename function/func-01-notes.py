# ============================================================
# Topic: Function Parameters, Local Scope & Global Scope
# ============================================================

# A variable created outside a function is called a Global Variable.
# It can be accessed from anywhere in the program.

# Example:
name = "Rinkesh"


# ------------------------------------------------------------
# Function Parameter
# ------------------------------------------------------------

# The parameter (name) is a Local Variable.
# It exists only inside the function.

def print_name(name):
    print(name)


# ------------------------------------------------------------
# Local Scope
# ------------------------------------------------------------

# Variables created inside a function belong only to that function.
# They are automatically destroyed after the function finishes.

def demo():
    city = "Delhi"
    print(city)


# city cannot be accessed here.
# print(city)   # NameError


# ------------------------------------------------------------
# Same Variable Name (Shadowing)
# ------------------------------------------------------------

# The local variable can have the same name as a global variable.
# The local variable temporarily hides (shadows) the global variable
# inside the function.

name = "Rinkesh"

def print_name(name):
    print(name)                  # Rinkesh
    name = "Rinkesh Kumar"
    print(name)                  # Rinkesh Kumar

print(name)                      # Rinkesh
print_name(name)
print(name)                      # Rinkesh


# Output:
# Rinkesh
# Rinkesh
# Rinkesh Kumar
# Rinkesh


# ------------------------------------------------------------
# Does changing the local variable affect the global variable?
# ------------------------------------------------------------

# No.
# Changing a local variable does NOT change the global variable.

name = "Rinkesh"

def change(name):
    name = "Kumar"

change(name)

print(name)

# Output:
# Rinkesh


# ------------------------------------------------------------
# Why?
# ------------------------------------------------------------

# Python creates a new local variable for the function parameter.
# The global variable remains unchanged.

# Global
# name = "Rinkesh"

# Local (inside function)
# name = "Kumar"


# ------------------------------------------------------------
# Modifying a Global Variable
# ------------------------------------------------------------

# To modify the global variable inside a function,
# use the global keyword.

name = "Rinkesh"

def change():
    global name
    name = "Rinkesh Kumar"

change()

print(name)

# Output:
# Rinkesh Kumar


# ------------------------------------------------------------
# Interview Notes
# ------------------------------------------------------------

# Q. Can a local variable and global variable have the same name?
# Ans: Yes.

# Q. Which variable is used inside the function?
# Ans: The local variable (parameter).

# Q. Does changing a local variable affect the global variable?
# Ans: No.

# Q. How can we modify a global variable inside a function?
# Ans: By using the global keyword.


# ------------------------------------------------------------
# Quick Revision
# ------------------------------------------------------------

# ✔ Variable outside function  -> Global Variable
# ✔ Variable inside function   -> Local Variable
# ✔ Function parameter         -> Local Variable
# ✔ Local variable hides the global variable (Shadowing)
# ✔ Local changes do NOT affect the global variable
# ✔ Local variables are destroyed after the function ends
# ✔ Use 'global' keyword to modify a global variable