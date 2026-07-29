from pydantic import BaseModel
from typing import Dict

class Classroom(BaseModel):
    students: Dict[int, str]

classroom = Classroom(
    students={
        1: "Rinkesh",
        2: "Rahul",
        3: "Amit"
    }
)

print(classroom)