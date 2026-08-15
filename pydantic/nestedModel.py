from pydantic import BaseModel

class Address(BaseModel):
    landmark:str
    city:str
    pincode:int
    state:str
    country:str
    
    


class User(BaseModel):
    id:int
    name:str
    address:Address
    
    
    

print(User(**{"id":1,"name":"Rinkesh","address":{"landmark":"Subhash Chowk","city":"FBD","pincode":"121005","state":"HR","country":"India"}}))        