user_list = ["Rinkesh","Abhishek","Nitish"]
user_amount = [100,600,445]

for name, amount in zip(user_list, user_amount):
    print(name, "has ₹", amount)
