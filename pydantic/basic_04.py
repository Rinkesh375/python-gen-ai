from pydantic import BaseModel
from typing import List, Dict

class Company(BaseModel):
    employees: List[Dict[str, str]]

company = Company(
    employees=[
        {"name": "Rinkesh", "role": "Developer"},
        {"name": "Rahul", "role": "Tester"}
    ]
)

print(company)