"""
Multiple Assignment and Variable Swapping

Multiple Assignment:
- Python allows assigning multiple values to multiple variables in one line.
- This is called multiple assignment (or tuple unpacking).

Example:
user1, user2 = "Rinkesh", "Nitish"

Equivalent to:
user1 = "Rinkesh"
user2 = "Nitish"

Variable Swapping:
- Python can swap variable values without using a temporary variable.

Example:
user1, user2 = user2, user1

How it works:
1. Python evaluates the right side first.
2. It creates a temporary tuple with the current values.
3. Then it unpacks the tuple into the variables on the left.

Before:
user1 = "Rinkesh"
user2 = "Nitish"

After:
user1 = "Nitish"
user2 = "Rinkesh"

Benefits:
- Cleaner code
- No extra temporary variable required
- Easy and Pythonic way to swap values
"""