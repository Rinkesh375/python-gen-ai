user = dict(name="Rinkesh",isMarried=False,age="Unknown",city="FBD",State="HR")
print(user)
print(user["name"])
# print(user["names"])
# print(user["nam"])


# In a Python dictionary, keys must be strings
user2 = {"name":"Nitish","age":"unknow"}
user2["isMarried"]= True

print(user2)
print(user2['isMarried'])

del user2["name"]
print(user2)


print("name" in user)
print("city" in user2)



print(user.keys())
print(user.values())
print(user)
print(user.pop("name"))
print(user)
print(user.items())
print(user.popitem())
print(user)