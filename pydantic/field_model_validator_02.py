from typing import Annotated

from pydantic import (
    BaseModel,
    StringConstraints,
    field_validator,
    model_validator,
)


class UserName(BaseModel):
    user_name: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            min_length=3,
            max_length=30,
            pattern=r"^[a-zA-Z0-9_]+$"
        )
    ]

    @field_validator("user_name")
    @classmethod
    def username_cannot_be_admin(cls, value: str):
        if value.lower() == "admin":
            raise ValueError(
                "Username 'admin' is reserved."
            )
        return value


class Password(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def validate_passwords(self):
        if self.password != self.confirm_password:
            raise ValueError(
                "Passwords do not match."
            )
        return self