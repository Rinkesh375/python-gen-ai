flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        print(f"flavour:{flavour}")
        continue

    if flavour == "Discontinued":
        print(f"Discontoinued item found {flavour}")
        break
    
print(f"flavour:{flavour}")
