from pydantic import BaseModel, field_validator, model_validator


class User_name(BaseModel):
    user_name:str
    
    @field_validator("user_name")
    def username_length_checker(cls,value):
        if (len(value) < 1):
            raise ValueError("user_name must be greater than equal to 1 character")
        return value
    
    
    
class Password(BaseModel):
    password:str
    confirm_password:str
    
    @model_validator(mode="after")
    def password_matcher(values):
        if (values.password != values.confirm_password):
            raise ValueError("password and confirm password must be same")
        return values        
    
    
  

# print(User_name(user_name="Rinkesh"))  
# print(User_name(user_name="")) 
print(Password(**{"confirm_password":"1245","password":"124"}))