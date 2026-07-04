# ==========================================
# continue and break Notes
# ==========================================

# continue
# Skips the remaining code in the current
# iteration and moves to the next iteration.

# break
# Immediately exits the loop completely.

# Example

for item in items:

    if item == "Skip":
        continue

    if item == "Stop":
        break

# Important

# continue → Skip current iteration.

# break → Stop the entire loop.

# Loop variable

# The loop variable still exists after
# the loop ends.

# If break stops the loop,
# the variable contains the value
# where break occurred.

# Rule to Remember

# continue = Skip

# break = Stop