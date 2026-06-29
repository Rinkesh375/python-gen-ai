"""
String Encoding in Python

- Python strings are stored as Unicode.
- encode() converts a Unicode string into bytes.
- By default, encode() uses UTF-8 encoding.
- The returned object is of type 'bytes'.

Example:
my_string = "café"

print(my_string)
# Output: café

print(my_string.encode())
# Output: b'caf\\xc3\\xa9'

Explanation:
- 'b' indicates a bytes object.
- 'é' is represented by two UTF-8 bytes: \\xc3\\xa9.

decode() converts bytes back into a string.

Example:
my_bytes = my_string.encode()
print(my_bytes.decode())
# Output: café

Remember:
String (Unicode) --encode()--> Bytes
Bytes --decode()--> String
"""