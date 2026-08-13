from typing import Annotated

from pydantic import (
    BaseModel,
    Field,
    StringConstraints,
    computed_field,
)


class Cart(BaseModel):
    id: int

    name: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            min_length=2,
            max_length=100,
        )
    ]

    price: float = Field(
        gt=0,
        description="Product price"
    )

    qty: int = Field(
        gt=0,
        description="Product quantity"
    )

    @computed_field
    @property
    def total_price(self) -> float:
        return round(self.price * self.qty, 2)