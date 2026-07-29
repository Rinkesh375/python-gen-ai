from pydantic import BaseModel
from typing import List, Union

class Data(BaseModel):
    values: List[Union[str, int, bool]]

data = Data(
    values=[
        "Python",
        100,
        True
    ]
)

print(data)