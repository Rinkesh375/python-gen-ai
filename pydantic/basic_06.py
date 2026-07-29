from pydantic import BaseModel
from typing import Dict, Any

class User(BaseModel):
    profile: Dict[str, Any]

user = User(
    profile={
        "name": "Rinkesh",
        "age": 28,
        "married": False,
        "skills": ["Python", "React"],
        "address": {
            "city": "Faridabad",
            "state": "Haryana"
        }
    }
)

print(user)