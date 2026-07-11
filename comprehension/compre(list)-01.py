"""

users = ["Rinkesh","Nitish","Abhishek","Pulkit","Manish","Rajesh","Sumit"]

users2 = [tea for tea in users if tea in ("Rinkesh", "Nitish" ,"Ma","Karan")]

print(users2)

"""



"""


users = [
    {"name":"Rinkesh","age":15},
    {"name":"Nitish","age":24},
    {"name":"Mukesh","age":5},
    {"name":"Manish","age":40},
    {"name":"Tanvir","age":18}
]


eligibleVotes = [user for user in users if user["age"]>=18]

print(eligibleVotes)


"""
