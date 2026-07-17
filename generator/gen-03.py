def infinite_call_generator():
    count = 1

    while True:
        yield f"Value is {count}"
        count += 1


infiniteCount = infinite_call_generator()

for index, value in enumerate(infiniteCount, start=1):
    print(value)

    if index == 10:
        break