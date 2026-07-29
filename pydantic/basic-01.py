from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str
    Married:bool
    
    

user_1 = {"id":1,"name":"Rinkesh","Married":False}
user_2 = {"id":1,"name":"Rinkesh","Married":0}
user_3 = {"id":"3","name":"Rinkesh","Married":False}
user_4 =  {"id":"a","name":"Rinkesh","Married":False}
user_5 =  {"id":"1","name":"Rinkesh","Married":"True"}

userOne = User(**user_1)
userTwo = User(**user_2)
userThree = User(**user_3)
userFour = User(**user_4)
userFive = User(**user_5)
print(userOne)
print(userTwo)
print(userThree)
print(userFour)
print(userFive)