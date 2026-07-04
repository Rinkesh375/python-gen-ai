user = ["Rinkesh", "Nitish","Abhishek","Vijay","Sunil","Pulkit"]

while (name := input("What is your name?").capitalize()) not in user:
    print(f"sorry you are not invited in party:{name}")
    
print(f"Congrats you are invited {name}")