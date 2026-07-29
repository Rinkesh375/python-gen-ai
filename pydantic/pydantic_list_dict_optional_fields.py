"""
==========================================================
Topic: Pydantic List, Dict & Optional Fields
File : pydantic_list_dict_optional_fields.py
==========================================================

Required Package
----------------

pip install pydantic

==========================================================
Code
==========================================================

from pydantic import BaseModel
from typing import List, Dict, Optional

class CartItem(BaseModel):
    id: int
    items: List[str]
    qtyItems: Dict[str, int]
    couponCode: Optional[str] = None

cart1 = CartItem(
    id=1,
    items=["Keyboard", "Mouse", "Earphone"],
    qtyItems={"Keyboard":1, "Mouse":5}
)

print(cart1)

==========================================================
1. Hinglish Explanation
==========================================================

Sabse pehle imports ko samajhte hain.

----------------------------------------------------------
Import 1
----------------------------------------------------------

from pydantic import BaseModel

BaseModel ka kaam hai

✔ Data Validate karna

✔ Data Type Check karna

✔ Type Convert karna (agar possible ho)

✔ Invalid data par ValidationError dena

----------------------------------------------------------
Import 2
----------------------------------------------------------

from typing import List, Dict, Optional

Ye Python ke Type Hints hain.

Ye batate hain ki kis field me kis type ka data
aana chahiye.

----------------------------------------------------------
List
----------------------------------------------------------

List ka matlab hai

Ek ordered collection.

Example

["Keyboard", "Mouse", "Earphone"]

Yaha sirf String values honi chahiye.

List[str]

Matlab

List ke andar har value String honi chahiye.

✔ Correct

["Pen", "Book"]

✔ Correct

["Laptop", "Mouse"]

❌ Wrong

["Laptop", 100]

Kyuki 100 String nahi hai.

----------------------------------------------------------
Dict
----------------------------------------------------------

Dict ka matlab

Key : Value pair

Example

{
    "Keyboard": 1,
    "Mouse": 5
}

Dict[str, int]

Matlab

Key

↓

String

Value

↓

Integer

✔ Correct

{
    "Keyboard":1,
    "Mouse":5
}

❌ Wrong

{
    100: "Keyboard"
}

Kyuki

Key Integer hai

Value String hai

Expected ulta tha.

----------------------------------------------------------
Optional
----------------------------------------------------------

Optional[str]

Matlab

Ye field ho bhi sakti hai

Aur nahi bhi.

Agar value nahi doge

To

None

assign ho jayega.

Example

couponCode=None

Ya

couponCode="SAVE20"

Dono valid hain.

==========================================================
Class Explanation
==========================================================

class CartItem(BaseModel):

Ye shopping cart ka model hai.

----------------------------------------------------------

id:int

Cart ka unique ID.

Required Field.

----------------------------------------------------------

items:List[str]

Shopping cart ke andar products ki list.

Har item String hona chahiye.

----------------------------------------------------------

qtyItems:Dict[str,int]

Har product ki quantity.

Example

Keyboard

↓

1

Mouse

↓

5

----------------------------------------------------------

couponCode:Optional[str]=None

Coupon optional hai.

Agar customer coupon use nahi kare

To automatically

None

set ho jayega.

==========================================================
Object Creation
==========================================================

cart1 = CartItem(

    id=1,

    items=[
        "Keyboard",
        "Mouse",
        "Earphone"
    ],

    qtyItems={
        "Keyboard":1,
        "Mouse":5
    }

)

Step-by-Step

id

↓

1

✔ Valid

---------------------

items

↓

List

Har item String hai.

✔ Valid

---------------------

qtyItems

↓

Dictionary

Keyboard

↓

1

Mouse

↓

5

Keys

↓

String

Values

↓

Integer

✔ Valid

---------------------

couponCode

Nahi diya.

Automatically

None

assign ho jayega.

==========================================================
Output
==========================================================

CartItem(

id=1,

items=['Keyboard', 'Mouse', 'Earphone'],

qtyItems={

'Keyboard':1,

'Mouse':5

},

couponCode=None

)

==========================================================
Better Real-World Example 1
==========================================================

Amazon Cart

cart = CartItem(

    id=201,

    items=[

        "Laptop",

        "Mouse",

        "Bag"

    ],

    qtyItems={

        "Laptop":1,

        "Mouse":2,

        "Bag":1

    },

    couponCode="SAVE20"

)

Customer ne coupon use kiya.

Coupon

↓

SAVE20

==========================================================
Better Real-World Example 2
==========================================================

Restaurant Order

class Order(BaseModel):

    tableNo:int

    foods:List[str]

    quantity:Dict[str,int]

    specialInstruction:Optional[str]=None

order = Order(

    tableNo=12,

    foods=[

        "Pizza",

        "Burger",

        "Coke"

    ],

    quantity={

        "Pizza":2,

        "Burger":1,

        "Coke":3

    }

)

Agar customer special instruction na de

To

specialInstruction

↓

None

==========================================================
Better Real-World Example 3
==========================================================

Student Courses

class Student(BaseModel):

    id:int

    name:str

    courses:List[str]

    marks:Dict[str,int]

    remarks:Optional[str]=None

student = Student(

    id=1,

    name="Rinkesh",

    courses=[

        "Python",

        "React",

        "SQL"

    ],

    marks={

        "Python":95,

        "React":88,

        "SQL":90

    }

)

Ye pattern school management systems me
bahut common hai.

==========================================================
Common Mistakes
==========================================================

❌ Wrong

items=[

    "Keyboard",

    10

]

Reason

10 String nahi hai.

----------------------------------------------------------

❌ Wrong

qtyItems={

    "Keyboard":"Five"

}

Reason

Quantity Integer honi chahiye.

----------------------------------------------------------

❌ Wrong

couponCode=123

Reason

Coupon String hona chahiye.

==========================================================
Interview Questions
==========================================================

Q. List[str] ka matlab kya hai?

Answer

List ke andar har value String hogi.

----------------------------------------------------------

Q. Dict[str,int] ka matlab kya hai?

Answer

Dictionary ki key String hogi
aur value Integer hogi.

----------------------------------------------------------

Q. Optional[str] ka matlab?

Answer

Field optional hai.

Value

String

ya

None

ho sakti hai.

==========================================================
Quick Revision
==========================================================

List[str]

↓

Multiple Strings

-----------------------

Dict[str,int]

↓

String Key

↓

Integer Value

-----------------------

Optional[str]

↓

String

or

None

==========================================================



==========================================================
2. English Explanation
==========================================================

Let's understand the imports first.

----------------------------------------------------------
BaseModel
----------------------------------------------------------

BaseModel validates incoming data before creating
a Python object.

It

✔ Validates data

✔ Checks data types

✔ Converts compatible values

✔ Raises ValidationError when needed

----------------------------------------------------------
List
----------------------------------------------------------

List[str]

Means

A list where every element must be a string.

Example

["Keyboard", "Mouse", "Earphone"]

----------------------------------------------------------
Dict
----------------------------------------------------------

Dict[str, int]

Means

Dictionary

Key

↓

String

Value

↓

Integer

Example

{

"Keyboard":1,

"Mouse":5

}

----------------------------------------------------------
Optional
----------------------------------------------------------

Optional[str]

Means

The field may contain

A String

or

None

If omitted,

Pydantic automatically assigns

None

==========================================================
Class Explanation
==========================================================

id:int

Required integer.

----------------------------------------------------------

items:List[str]

A list of product names.

Every element must be a string.

----------------------------------------------------------

qtyItems:Dict[str,int]

Stores product quantity.

Keys

↓

Product names

Values

↓

Quantity

----------------------------------------------------------

couponCode:Optional[str]=None

Coupon code is optional.

If not supplied,

Pydantic sets

None.

==========================================================
Object Validation
==========================================================

id

↓

Integer

✔ Valid

----------------

items

↓

List of strings

✔ Valid

----------------

qtyItems

↓

Dictionary

Keys

↓

Strings

Values

↓

Integers

✔ Valid

----------------

couponCode

↓

Automatically

None

==========================================================
Output
==========================================================

CartItem(

id=1,

items=['Keyboard', 'Mouse', 'Earphone'],

qtyItems={

'Keyboard':1,

'Mouse':5

},

couponCode=None

)

==========================================================
Production Example 1
==========================================================

FastAPI Shopping Cart

Incoming JSON

{

"id":101,

"items":[

"Laptop",

"Mouse"

],

"qtyItems":{

"Laptop":1,

"Mouse":2

}

}

Pydantic validates everything before
saving to the database.

==========================================================
Production Example 2
==========================================================

Food Delivery App

Order

↓

Food Items

↓

Quantity

↓

Coupon Code

All are validated using BaseModel.

==========================================================
Production Example 3
==========================================================

Online Learning Platform

Student

↓

Courses (List)

↓

Marks (Dictionary)

↓

Scholarship Code (Optional)

This structure is very common in production
backend applications.

==========================================================
Key Points
==========================================================

✔ List[str] → List of strings.

✔ Dict[str,int] → String keys and Integer values.

✔ Optional[str] → String or None.

✔ Missing optional fields automatically become None.

✔ Widely used in FastAPI, REST APIs,
E-commerce, Inventory Systems,
School Management Systems,
and Order Management applications.

==========================================================

"""