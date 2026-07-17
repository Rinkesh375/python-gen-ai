def print_alphabets():
    yield "A"
    yield "B"
    yield "C"
    yield "D"
    yield "E"
    yield "F"
    yield "G"
    
    
alphabets= print_alphabets()
# print(alphabets)    
    
    
# for ch in alphabets:
#     print(f"This is {ch}")    
    
print(next(alphabets))    