amount = int(input("Delivery amount? "))

if amount < 0:
    print("Please enter a valid amount.")
    exit()

amount = amount if amount > 300 else amount + 30

print(amount)