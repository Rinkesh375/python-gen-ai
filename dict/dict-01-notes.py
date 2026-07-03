# Dictionary
# ----------
# A dictionary stores data as key:value pairs.

# Correct
user = {
    "name": "Nitish",
    "age": "unknown"
}

print(user)

# Incorrect
# user = {name: "Nitish", age: "unknown"}
# Because 'name' and 'age' are treated as variables.
# If they are not defined, Python raises NameError.