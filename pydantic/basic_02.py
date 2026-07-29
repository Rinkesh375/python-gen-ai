from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    inStock:bool
    price:float
    discount_coupon:bool = False
    


p1 = Product(id=1,name="Iphone",inStock=True,price=32)   
p2 = Product(name="Iphone",inStock=True,price=32)
print(p1,p2)