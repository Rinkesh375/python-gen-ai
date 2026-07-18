"""
=========================================
Topic: Decorator Example - Authorization
=========================================

What is this Decorator?
-----------------------
This decorator checks whether the user
is an admin before allowing the original
function to execute.

If the user is not an admin,
the original function will not run.

=========================================
Example
=========================================
"""

def authorization(fn):

    def wrapper(name, user_role="user"):

        if user_role == "admin":
            fn(name)
        else:
            print("Access Denied! Admin permission required.")

    return wrapper


@authorization
def admin_panel(name):
    print(f"Welcome Admin: {name}")


# Admin User
admin_panel("Rinkesh", "admin")

print("-" * 30)

# Normal User
admin_panel("Rahul", "user")


"""
Output
------

Welcome Admin: Rinkesh
------------------------------
Access Denied! Admin permission required.

=========================================
How it Works Internally
=========================================

Python sees

@authorization
def admin_panel(name):
    ...

Internally Python converts it into

def admin_panel(name):
    ...

admin_panel = authorization(admin_panel)

Step 1
------
Python creates the original function.

Step 2
------
authorization(admin_panel) is called.

Here,

fn = Original admin_panel

Step 3
------
authorization() returns wrapper()

Step 4
------
Now,

admin_panel = wrapper

Step 5
------
Calling

admin_panel("Rinkesh", "admin")

actually calls

wrapper("Rinkesh", "admin")

Execution Flow
--------------

admin_panel("Rinkesh", "admin")
            │
            ▼
        wrapper()
            │
            ▼
Check user role
            │
      ┌─────┴─────┐
      │           │
    Admin       Not Admin
      │           │
      ▼           ▼
Call fn()    Print Error
      │
      ▼
Original Function

=========================================
Notes
=========================================

✔ Decorator receives another function.
✔ Wrapper checks the user's role.
✔ If role is "admin", the original function runs.
✔ Otherwise, access is denied.
✔ @authorization is shorthand for:

    admin_panel = authorization(admin_panel)

Real-life Example
-----------------
Think of a security guard at an office.

Visitor
   │
   ▼
Security Check (Decorator)
   │
   ├── Admin → Enter Office
   └── User  → Access Denied

The office (original function) never
checks permissions itself.

The decorator handles it.
"""