# ==========================================
# global vs nonlocal Notes
# ==========================================

# global

# Accesses and modifies a variable
# from the global scope.

x = 10

def func():
    global x
    x += 1

# nonlocal

# Accesses and modifies a variable
# from the nearest enclosing function.

def outer():

    x = 10

    def inner():
        nonlocal x
        x += 1

# Difference

# global
# → Global Scope

# nonlocal
# → Enclosing Function Scope

# LEGB Rule

# L → Local
# E → Enclosing
# G → Global
# B → Built-in

# Rule to Remember

# global → Outside the function

# nonlocal → Parent function