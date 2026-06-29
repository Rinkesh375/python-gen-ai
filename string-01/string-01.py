my_string = "café"
print(my_string)

encoded_string = my_string.encode("utf-8")
decoded_string = encoded_string.decode("utf-8")

print(encoded_string)
print(decoded_string)