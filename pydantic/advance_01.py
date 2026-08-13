from pydantic import BaseModel, field_validator, EmailStr, model_validator, Field
from datetime import datetime


class Person(BaseModel):
    firstName:str
    lastName:str
    
    @field_validator("firstName","lastName")
    @classmethod
    def check_name_capitalization(cls,value):
        isCapitalize = value.istitle()
        if not isCapitalize:
            raise ValueError("first name, last name first character must be capital in capital letter")
        return value
    
    
    

# nameOne = Person(**{"firstName":"Rinkesh","lastName":"Kumar"})
# nameTwo = Person(**{"firstName":"inkesh","lastName":"Kumar"})
# print(nameOne)    
# print(nameTwo)









class User(BaseModel):
    email: EmailStr
    @field_validator("email")
    @classmethod
    def emailLower(cls,value):
        return value.lower()
    

# print(User(**{"email":"rinkesh@pharmaedge.ai"}))    
# print(User(**{"email":"      rinkesh@pharmaedge.ai                "}))  
# print(User(**{"email":"RINKESH@pharmaedge.ai"}))  




class Product(BaseModel):
    price:int
    @field_validator("price",mode="before")
    @classmethod
    def priceValiator(cls,value):
        if (not isinstance(value,str)):
            raise TypeError("price must be string e.g-> $4")
        return int(value.replace("$","") )
    
    
# priceOne = Product(**{"price":"$4"})
# priceTwo = Product(**{"price":4})
# print(priceTwo)
# print(priceOne,type(priceOne.price))    
    
    
    



class Meeting(BaseModel):
    start_time: datetime = Field(
        description="Meeting start time"
    )

    end_time: datetime = Field(
        description="Meeting end time"
    )

    @model_validator(mode="after")
    def validate_time_range(self):
        if self.start_time >= self.end_time:
            raise ValueError(
                "Start time must be earlier than end time."
            )

        return self
 
 
 
        
booking = Meeting(
    start_time="2026-08-01T10:00:00",
    end_time="2026-08-01T11:30:00"

)

        
bookingTwo = Meeting(
    start_time="2026-08-01T10:00:00",
    end_time="2026-07-01T11:30:00"

)

print(booking)        