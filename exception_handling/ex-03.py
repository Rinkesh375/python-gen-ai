def process_order(order_type, quantity):
    try:

        # Validate quantity
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be an integer greater than 0.")

        # Menu
        menu = {
            "masala": 50,
            "ginger": 60,
            "elaichi": 70
        }

        # Check order type
        price = menu[order_type]

        total = price * quantity

        print(f"{order_type.title()} price will be ₹{total}")

    except KeyError:
        print(f"{order_type} is not available in the menu.")

    except ValueError as error:
        print(error)


process_order("masala", 3)
process_order("masa", 3)
process_order("masala", "chunnu")
process_order("masala", -5)