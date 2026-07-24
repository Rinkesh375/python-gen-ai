class InvalidError(Exception):
    pass


def order_chai(name, qty):
    menu = {
        "ginger": 50,
        "masala": 40
    }

    try:
        # Validate menu
        if name not in menu:
            raise InvalidError(f"{name} is not available in the menu.")

        # Convert quantity into integer
        try:
            qty = int(qty)
        except ValueError:
            raise TypeError(f"{qty} must be a valid integer.")

        # Quantity should be greater than 0
        if qty <= 0:
            raise ValueError("Quantity must be greater than 0.")

        return menu[name] * qty

    except Exception as error:
        return error


print(order_chai("ginger", 2))
print(order_chai("masala", 4))
print(order_chai("ginger", "4"))
print(order_chai("ginger", "abc"))
print(order_chai("ginger", -2))
print(order_chai("coffee", 2))