"""

users = ["Rinkesh","Nitish","Abhishek","Pulkit","Manish","Rajesh","Sumit","Nitish","nitish","rinkesh","Rinkesh","rinkesh"]


users2 = {user for user in users}

unique_users = {
    f"{user.capitalize()} Kumar" for user in users
}

print(users2)

print(unique_users)

"""



