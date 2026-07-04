# ==========================================
# Python match-case Notes
# ==========================================

# match-case was introduced in Python 3.10.

# It is used to compare ONE variable against
# multiple fixed values.

# It is similar to switch-case in Java,
# JavaScript, and C#.

# General Syntax

# match variable:
#     case value1:
#         # Code
#     case value2:
#         # Code
#     case value3:
#         # Code
#     case _:
#         # Default Code

# match
# Starts pattern matching.

# case
# Checks whether the variable matches a value.

# case _
# Default case.
# Executes when no other case matches.

# Use .lower() when taking string input
# so comparisons become case-insensitive.

# Example:
#
# seat = input().lower()

# match seat:
#     case "ac":
#         print("AC Coach")
#     case "sleeper":
#         print("Sleeper Coach")
#     case _:
#         print("Invalid Seat")

# Best Practice
# ✔ Use match-case when comparing one
#   variable against many fixed values.
#
# ✔ Use if-elif-else for ranges or
#   complex conditions.

# Common Mistakes

# ❌ Using match-case in Python < 3.10

# ❌ Forgetting the colon (:)

# ❌ Using default instead of case _

# Rule to Remember
# match chooses ONE variable.
# case checks ONE possible value.
# case _ handles everything else.