import tiktoken

text  = "Hey There! My name is Rinkesh"

enc = tiktoken.encoding_for_model("gpt-4o")

token = enc.encode(text)

#
print(token)

decodeVaule = enc.decode([25216, 3274, 0, 3673, 1308, 382, 460, 881, 8382])
print(decodeVaule)