"""
==========================================================
Topic: Pydantic Default Values & Required Fields
File : pydantic_default_values_and_required_fields.py
==========================================================

Required Package
----------------

pip install pydantic

==========================================================
1. Hinglish Explanation
==========================================================

Code
----

from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    inStock: bool
    price: float
    discount_coupon: bool = False

Sabse pehle samajhte hain BaseModel kya kar raha hai.

BaseModel ka kaam hai:

✔ Data validate karna
✔ Data type check karna
✔ Agar possible ho to type convert karna
✔ Default values provide karna
✔ Invalid data hone par ValidationError dena

----------------------------------------------------------
Class Explanation
----------------------------------------------------------

class Product(BaseModel):

Hum Product naam ka model bana rahe hain.

Ye model batata hai ki Product object me
kaun-kaun si fields honi chahiye.

----------------------------------------------------------

id: int

Har product ka unique ID hoga.

Ye Required Field hai.

Matlab value deni hi padegi.

Example

1
100
250

----------------------------------------------------------

name: str

Product ka naam.

Ye bhi Required Field hai.

Example

"Iphone"

"Laptop"

----------------------------------------------------------

inStock: bool

Product stock me hai ya nahi.

Sirf

True

ya

False

accept karega.

----------------------------------------------------------

price: float

Product ki price.

Float expected hai.

Lekin agar integer doge,

Pydantic automatically convert kar dega.

32

↓

32.0

----------------------------------------------------------

discount_coupon: bool = False

Yaha pe ek Default Value di gayi hai.

Agar user value nahi dega,

to automatically

False

set ho jayega.

Ye Optional Field ban gayi.

==========================================================
Product 1
==========================================================

p1 = Product(
    id=1,
    name="Iphone",
    inStock=True,
    price=32
)

Step-by-Step

id

1

✔ Correct

----------------

name

"Iphone"

✔ Correct

----------------

inStock

True

✔ Correct

----------------

price

32

Expected

float

Pydantic convert karega

32

↓

32.0

----------------

discount_coupon

Value nahi di.

To automatically

False

assign ho jayega.

Final Object

Product(
    id=1,
    name='Iphone',
    inStock=True,
    price=32.0,
    discount_coupon=False
)

==========================================================
Product 2
==========================================================

p2 = Product(
    name="Iphone",
    inStock=True,
    price=32
)

Yaha id missing hai.

id Required Field hai.

Isliye object create nahi hoga.

Output

ValidationError

id
Field required

Program isi line par stop ho jayega.

print() execute nahi hoga.

==========================================================
Required vs Optional Fields
==========================================================

Required

id:int

name:str

price:float

inStock:bool

-------------------------

Optional

discount_coupon:bool=False

Reason

Kyuki uske paas already default value hai.

==========================================================
Program Flow
==========================================================

Create p1

↓

Validation Success

↓

Object Created

↓

Create p2

↓

Validation Failed

↓

ValidationError

↓

Program Stops

==========================================================
Better Production Code
==========================================================

from pydantic import ValidationError

try:

    product = Product(
        name="Iphone",
        inStock=True,
        price=32
    )

    print(product)

except ValidationError as e:

    print(e)

Production code me hamesha ValidationError
handle karna chahiye.

==========================================================
Real-World Example
==========================================================

Suppose frontend se ye data aaya.

{
    "id":101,
    "name":"Samsung S25",
    "price":950,
    "inStock":True
}

Backend

product = Product(**request_data)

Pydantic automatically karega

950

↓

950.0

Aur

discount_coupon

automatically

False

kar dega.

Ab database me clean data save hoga.

==========================================================
Another Real-World Example
==========================================================

E-commerce Website

class Product(BaseModel):

    id:int
    title:str
    quantity:int
    available:bool=True
    price:float
    free_shipping:bool=False

Agar frontend sirf ye bheje

{
    "id":101,
    "title":"Mouse",
    "quantity":5,
    "price":25
}

Automatically

available=True

free_shipping=False

ho jayega.

Frontend ko unnecessary values bhejne ki
zarurat hi nahi.

==========================================================
Common Mistake
==========================================================

Galat

Product(
    name="Iphone",
    price=100
)

Error

id missing

inStock missing

----------------------------------------------------------

Sahi

Product(
    id=1,
    name="Iphone",
    price=100,
    inStock=True
)

==========================================================
Interview Questions
==========================================================

Q. Required field kya hoti hai?

Answer

Jiski default value nahi hoti.

----------------------------------------------------------

Q. Optional field kya hoti hai?

Answer

Jiski default value already define hoti hai.

----------------------------------------------------------

Q. Integer ko float me convert karega?

Yes.

100

↓

100.0

==========================================================
Quick Revision
==========================================================

BaseModel

↓

Validate

↓

Convert Types

↓

Assign Default Values

↓

Return Python Object

==========================================================



==========================================================
2. English Explanation
==========================================================

Code
----

from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    inStock: bool
    price: float
    discount_coupon: bool = False

BaseModel validates incoming data before creating
a Python object.

It can

✔ Validate data

✔ Convert compatible types

✔ Apply default values

✔ Raise ValidationError for invalid data

----------------------------------------------------------
Class Explanation
----------------------------------------------------------

id: int

Unique product ID.

Required field.

----------------------------------------------------------

name: str

Product name.

Required field.

----------------------------------------------------------

inStock: bool

Indicates whether the product is available.

Required field.

----------------------------------------------------------

price: float

Expected to be a floating-point number.

If an integer is provided,

Pydantic converts it automatically.

32

↓

32.0

----------------------------------------------------------

discount_coupon: bool = False

This field has a default value.

If the user doesn't provide it,

Pydantic automatically sets

False.

This makes it an optional field.

==========================================================
Product 1
==========================================================

Product(
    id=1,
    name="Iphone",
    inStock=True,
    price=32
)

Validation

✔ id

✔ name

✔ inStock

✔ price

32

↓

32.0

discount_coupon

↓

False

Result

Product(
    id=1,
    name='Iphone',
    inStock=True,
    price=32.0,
    discount_coupon=False
)

==========================================================
Product 2
==========================================================

Product(
    name="Iphone",
    inStock=True,
    price=32
)

The id field is missing.

Since id is required,

Pydantic raises

ValidationError

The program stops before print() executes.

==========================================================
Required vs Optional Fields
==========================================================

Required

id

name

price

inStock

Optional

discount_coupon

because it has a default value.

==========================================================
Production Example
==========================================================

from pydantic import ValidationError

try:

    product = Product(...)

except ValidationError as e:

    print(e)

Always catch ValidationError when validating
external data.

==========================================================
Real-World Example
==========================================================

A FastAPI endpoint receives

{
    "id":101,
    "name":"Samsung S25",
    "price":950,
    "inStock":True
}

Internally,

Product(**request_data)

creates

Product(
    id=101,
    name="Samsung S25",
    price=950.0,
    inStock=True,
    discount_coupon=False
)

This ensures your backend always works
with clean and validated data.

==========================================================
Another Real-World Example
==========================================================

Inventory System

class InventoryItem(BaseModel):

    sku:int
    name:str
    quantity:int
    active:bool=True
    price:float

If active is not provided,

Pydantic automatically assigns

True.

This reduces unnecessary data sent
from the frontend.

==========================================================
Key Points
==========================================================

✔ Fields without default values are required.

✔ Fields with default values are optional.

✔ Pydantic automatically converts compatible types.

✔ Invalid or missing required fields raise
ValidationError.

✔ Commonly used in FastAPI, APIs,
microservices, and backend applications.

==========================================================

"""