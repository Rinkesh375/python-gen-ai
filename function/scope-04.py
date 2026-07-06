x = "Global"

def outer():

    x = "Outer"

    def inner():

        nonlocal x

        x = "Changed"

    inner()

    print(x)

outer()

print(x)