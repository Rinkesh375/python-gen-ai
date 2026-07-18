from functools import wraps
def outer(fn):
    @wraps(fn)
    def innererFun(value):
        print("this is inner") 
        fn(value) 
        print("This is inner-2")
    return innererFun    
         
         
         
@outer
def printValeFun(value):
    print(f"Value:{value}")
    
    
printValeFun(5)

print(printValeFun.__name__)