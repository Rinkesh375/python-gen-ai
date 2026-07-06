def outer():

    count = 10

    def inner():
        nonlocal count
        count += 1
        print(count)

    inner()

outer()