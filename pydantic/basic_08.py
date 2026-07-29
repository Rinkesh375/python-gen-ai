from pydantic import BaseModel
from typing import Dict, Union

class Product(BaseModel):
    info: Dict[str, Union[str, int, bool]]

product = Product(
    info={
        "name": "Keyboard",
        "price": 999,
        "available": True
    }
)

print(product)