x = "Global"

def outer():
    global x
    x = "Outer"

    def inner():

        global x
        x = "Changed"

    inner()

    print(x)

outer()

print(x)