# Dictionary update()
# -------------------
# update() copies all key:value pairs from one dictionary
# into another dictionary.

user1 = {
    "name": "Rinkesh",
    "city": "FBD"
}

extraInfo = {
    "mobile": "1234567890",
    "language": ["Hindi", "English"]
}

user1.update(extraInfo)

print(user1)

# Output:
# {
#   'name': 'Rinkesh',
#   'city': 'FBD',
#   'mobile': '1234567890',
#   'language': ['Hindi', 'English']
# }

# Rules:
# 1. New keys are added.
# 2. Existing keys are updated (overwritten).
# 3. Only the first dictionary changes.
# 4. The second dictionary remains unchanged.


"-------------------------------------------------------------------------------------------------------------------"


# Accessing Dictionary Values
# ---------------------------

# Using []
# Returns the value if the key exists.
# Raises KeyError if the key does not exist.

print(user1["state"])

# Using get()
# Returns the value if the key exists.
# If the key does not exist, it returns:
# - None (by default), or
# - the default value you provide.

print(user1.get("country", "No country key value available"))

# Difference:
# []    -> Error if key is missing.
# get() -> Safe. Returns default value instead of an error.