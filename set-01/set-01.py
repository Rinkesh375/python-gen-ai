user1 = {"Rinkesh","Nitish","Abhishek","Nitish"}

user2 = {"Abhishek","ABhishek","Karn","Arjun","Ajay","Vijay","Rinkesh"}

allUsers = user1 | user2

duplicateUsers = user1 & user2

print(allUsers)
print(duplicateUsers)

print(user1-user2)
# Return the elements that are present in the first set (user1) but NOT present in the second set (user2).

print("Rinkesh" in user2)
print("inkesh" in user2)
print("Nitish" in user2)