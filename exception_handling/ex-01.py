try:
    value = 10/0
    print(value)
except:
       print("This value can not be divied") 
       
       


try:
    value = 20/0
    print(value)
except ZeroDivisionError:
    print("Zero ZeroDivisionError occuring can not be divided by a number")
              