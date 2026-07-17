def infinite_call_generator():
    count = 1
    while True:
        yield f"Value is {count}"
        count += 1
        
        

infiniteCount = infinite_call_generator()

# print(next(infiniteCount))   
# print(next(infiniteCount))      
# print(next(infiniteCount)) 
# print(next(infiniteCount)) 
# print(next(infiniteCount)) 
# print(next(infiniteCount))


for value in  infiniteCount:
    print(value)