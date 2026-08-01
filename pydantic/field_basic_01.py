from typing import Annotated
from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    StringConstraints,
)


class Employee(BaseModel):
    """
    Employee Model
    """

    id: int = Field(
        ...,
        description="Unique Employee ID",
        examples=[1]
    )

    name: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True,
            min_length=2,
            max_length=50,
            pattern=r"^[A-Za-z ]+$"
        )
    ]

    email: EmailStr = Field(
        ...,
        description="Employee Email",
        examples=["rinkesh@pharmaedge.ai"]
    )

    department: str = Field(
        default="General",
        description="Employee Department",
        examples=["Engineering"]
    )

    salary: float = Field(
        ...,
        gt=0,
        le=10_000_000,
        description="Employee Salary",
        examples=[75000]
    )

    contact: Annotated[
        str,
        StringConstraints(
            pattern=r"^\d{10}$"
        )
    ]

    age: int = Field(
        ...,
        ge=18,
        le=58,
        description="Employee Age",
        examples=[28]
    )

    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Employee Discount Percentage",
        examples=[15]
    )


# ---------------------------------------------------
# ✅ Correct Example
# ---------------------------------------------------

employee = Employee(
    id=1,
    name="   Rinkesh Kumar   ",
    email="rinkesh@pharmaedge.ai",
    department="Engineering",
    salary=75000,
    contact="9136454545",
    age=28,
    discount=15
)

print(employee)


"""
Output

Employee(
    id=1,
    name='Rinkesh Kumar',
    email='rinkesh@pharmaedge.ai',
    department='Engineering',
    salary=75000.0,
    contact='9136454545',
    age=28,
    discount=15.0
)
"""


# ===================================================
# ❌ Wrong Example 1
# Only whitespace
# ===================================================

"""
Employee(
    id=1,
    name="     ",
    email="rinkesh@pharmaedge.ai",
    salary=75000,
    contact="9136454545",
    age=28,
    discount=15
)

Reason

strip_whitespace=True

"     "

↓

""

↓

Length becomes 0

↓

ValidationError
"""


# ===================================================
# ❌ Wrong Example 2
# Numbers inside name
# ===================================================

"""
Employee(
    id=1,
    name="Rinkesh123",
    email="rinkesh@pharmaedge.ai",
    salary=75000,
    contact="9136454545",
    age=28,
    discount=15
)

Reason

Name only allows letters and spaces.
"""


# ===================================================
# ❌ Wrong Example 3
# Invalid Email
# ===================================================

"""
Employee(
    id=1,
    name="Rinkesh Kumar",
    email="rinkeshexample.com",
    salary=75000,
    contact="9136454545",
    age=28,
    discount=15
)

Reason

Missing @
"""


# ===================================================
# ❌ Wrong Example 4
# Salary too high
# ===================================================

"""
Employee(
    id=1,
    name="Rinkesh Kumar",
    email="rinkesh@pharmaedge.ai",
    salary=99999999999,
    contact="9136454545",
    age=28,
    discount=15
)

Reason

Salary exceeds maximum limit.
"""


# ===================================================
# ❌ Wrong Example 5
# Contact contains letters
# ===================================================

"""
Employee(
    id=1,
    name="Rinkesh Kumar",
    email="rinkesh@pharmaedge.ai",
    salary=75000,
    contact="91364ABCDE",
    age=28,
    discount=15
)

Reason

Only digits are allowed.
Exactly 10 digits.
"""


# ===================================================
# ❌ Wrong Example 6
# Contact too short
# ===================================================

"""
Employee(
    id=1,
    name="Rinkesh Kumar",
    email="rinkesh@pharmaedge.ai",
    salary=75000,
    contact="91364",
    age=28,
    discount=15
)

Reason

Must contain exactly 10 digits.
"""


# ===================================================
# ❌ Wrong Example 7
# Age below minimum
# ===================================================

"""
Employee(
    id=1,
    name="Rinkesh Kumar",
    email="rinkesh@pharmaedge.ai",
    salary=75000,
    contact="9136454545",
    age=15,
    discount=15
)

Reason

Minimum allowed age is 18.
"""


# ===================================================
# ❌ Wrong Example 8
# Discount greater than 100
# ===================================================

"""
Employee(
    id=1,
    name="Rinkesh Kumar",
    email="rinkesh@pharmaedge.ai",
    salary=75000,
    contact="9136454545",
    age=28,
    discount=150
)

Reason

Discount must be between 0 and 100.
"""