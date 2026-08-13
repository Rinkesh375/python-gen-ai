from pydantic import BaseModel, field_validator

class Product(BaseModel):
    price: int

    @field_validator("price", mode="before")
    @classmethod
    def parse_price(cls, value):
        if not isinstance(value, str):
            raise ValueError("Price must be a string like '$4'.")

        if not value.startswith("$"):
            raise ValueError("Price must start with '$'.")

        numeric = value[1:]

        if not numeric.isdigit():
            raise ValueError("Price must contain only digits after '$'.")

        return int(numeric)