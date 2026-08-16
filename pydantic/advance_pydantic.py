from typing import List, Dict, Optional
from pydantic import BaseModel, Field

class Country(BaseModel):
    name:str
    code:str


class State(BaseModel):
    name:str
    country:Country
    

class City(BaseModel):
    name:str
    state:State

class Address(BaseModel):
    street:str
    city:City
    postal_code:str
    
    

class Organization(BaseModel):
    name:str
    headOffice:Address
    branches:List[Address] = Field(default_factory=[])                