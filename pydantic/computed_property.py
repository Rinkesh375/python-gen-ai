from pydantic import BaseModel, computed_field


class Cart(BaseModel):
    id:int
    name:str
    price:float
    qty:int
    
    @computed_field
    @property
    def total_price(self) -> float:
        return self.price*self.qty
    


productOne = Cart(**{"id":1,"name":"keyboard","price":100,"qty":100})
print(productOne)

print(productOne.total_price)
print(productOne.model_dump())

print(type(productOne.model_dump())) 