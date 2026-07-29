"""
==========================================================
Topic: Pydantic BaseModel - Data Validation & Type Conversion
File : pydantic_basemodel_validation_notes.py
==========================================================

Required Package
----------------

pip install pydantic

==========================================================
1. Hinglish Explanation
==========================================================

Code:
-----

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    Married: bool

Pehle samajhte hain ki BaseModel kya hai.

BaseModel Pydantic ka ek special class hai.

Iska kaam hai:

✅ Data ko validate karna
✅ Data ka type check karna
✅ Possible ho to automatically type convert karna
✅ Invalid data ho to error dena

Simple language me:

Agar koi user data API, database ya frontend se aaye,
to BaseModel check karega ki data sahi format me hai ya nahi.

----------------------------------------------------------
Class Explanation
----------------------------------------------------------

class User(BaseModel):

Hum ek User model bana rahe hain.

Is model ke andar 3 fields hain.

id: int

Matlab id integer honi chahiye.

------------------------

name: str

Matlab name string hona chahiye.

------------------------

Married: bool

Matlab sirf True ya False hona chahiye.

==========================================================
User 1
==========================================================

user_1 = {
    "id": 1,
    "name": "Rinkesh",
    "Married": False
}

userOne = User(**user_1)

Python internally:

User(
    id=1,
    name="Rinkesh",
    Married=False
)

Sabhi values already correct type ki hain.

Output

User(id=1, name='Rinkesh', Married=False)

==========================================================
User 2
==========================================================

user_2 = {
    "id":1,
    "name":"Rinkesh",
    "Married":0
}

Question:

0 bool kaise ban gaya?

Pydantic automatically convert karta hai.

0  -> False
1  -> True

Output

User(id=1, name='Rinkesh', Married=False)

==========================================================
User 3
==========================================================

user_3 = {
    "id":"3",
    "name":"Rinkesh",
    "Married":False
}

Yaha id string hai.

Lekin string ke andar number likha hua hai.

"3"

Pydantic sochta hai:

"Ye integer ban sakta hai."

Isliye automatically convert kar deta hai.

"3"

↓

3

Output

User(id=3, name='Rinkesh', Married=False)

==========================================================
User 4
==========================================================

user_4 = {
    "id":"a",
    "name":"Rinkesh",
    "Married":False
}

Ab id me "a" diya hai.

"a" ko integer me convert nahi kiya ja sakta.

Isliye validation fail ho jayegi.

Output

ValidationError

id
Input should be a valid integer

Program yahi par stop ho jayega.

Isliye niche wala code execute hi nahi hoga.

print(userFive)

kabhi run nahi hoga.

==========================================================
User 5
==========================================================

Ye code kabhi execute hi nahi karega
kyunki user_4 pe ValidationError aa chuki hai.

Agar user_4 hata dein to:

user_5 = {
    "id":"1",
    "name":"Rinkesh",
    "Married":"True"
}

Pydantic convert karega

"id"

"1"

↓

1

----------------

"True"

↓

True

Output

User(id=1, name='Rinkesh', Married=True)

==========================================================
Program Flow
==========================================================

User(**user_1)

↓

Validation

↓

Object Create

↓

User(**user_2)

↓

Validation

↓

Object Create

↓

User(**user_3)

↓

Validation

↓

Object Create

↓

User(**user_4)

↓

Validation Failed

↓

ValidationError

↓

Program Stops

==========================================================
Better Way
==========================================================

Har validation ko try-except me likho.

Example:

users = [user_1, user_2, user_3, user_4, user_5]

for data in users:
    try:
        user = User(**data)
        print(user)

    except Exception as e:
        print(e)

Ab ek data galat hone par bhi
baaki users validate ho jayenge.

==========================================================
Real-World Example
==========================================================

Suppose frontend se API request aayi.

Request Body

{
    "id":"101",
    "name":"Rinkesh",
    "Married":"False"
}

FastAPI automatically karega:

User(**request_data)

Pydantic convert karega:

id

"101"

↓

101

Married

"False"

↓

False

Ab backend ke paas clean data hoga.

Database me wrong type save nahi hogi.

Isi wajah se FastAPI aur Pydantic saath me
bahut use hote hain.

==========================================================
Important Notes
==========================================================

BaseModel automatically

✔ validates data

✔ converts compatible data

✔ raises ValidationError on invalid data

✔ makes API development much safer

==========================================================
Interview Questions
==========================================================

Q. Why use BaseModel?

Answer:

To validate incoming data and automatically convert
compatible values into the correct Python types.

----------------------------------------------------------

Q. Does Pydantic always convert types?

Answer:

No.

Only when conversion is possible.

"5"

↓

5

works

"a"

↓

int

does not work.

==========================================================
Quick Revision
==========================================================

BaseModel

↓

Validation

↓

Type Conversion

↓

Python Object

==========================================================



==========================================================
2. English Explanation
==========================================================

Code:
-----

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    Married: bool

BaseModel is a special class provided by Pydantic.

Its purpose is to:

• Validate incoming data.
• Check data types.
• Automatically convert compatible values.
• Raise an error if validation fails.

In simple words,

whenever data comes from an API, database,
or frontend, BaseModel makes sure that the
data matches the expected format.

----------------------------------------------------------
Class Explanation
----------------------------------------------------------

id: int

The id field must be an integer.

------------------------

name: str

The name field must be a string.

------------------------

Married: bool

The Married field must be a boolean value.

==========================================================
User 1
==========================================================

Input

{
    "id":1,
    "name":"Rinkesh",
    "Married":False
}

Everything is already the correct type.

Output

User(id=1, name='Rinkesh', Married=False)

==========================================================
User 2
==========================================================

Input

{
    "Married":0
}

Pydantic converts

0

↓

False

Output

User(id=1, name='Rinkesh', Married=False)

==========================================================
User 3
==========================================================

Input

"id":"3"

Since "3" is a numeric string,

Pydantic converts it into

3

Output

User(id=3, name='Rinkesh', Married=False)

==========================================================
User 4
==========================================================

Input

"id":"a"

The string "a" cannot be converted into an integer.

Pydantic raises

ValidationError

The program stops at this point.

==========================================================
User 5
==========================================================

This code never executes because the previous
validation already failed.

If user_4 is removed,

Pydantic converts

"id":"1"

↓

1

and

"True"

↓

True

Output

User(id=1, name='Rinkesh', Married=True)

==========================================================
Better Production Example
==========================================================

Instead of validating one object at a time,
use try-except.

for data in users:
    try:
        user = User(**data)
        print(user)

    except ValidationError as e:
        print(e)

This allows the application to continue even if
one record is invalid.

==========================================================
Real-World Use Case
==========================================================

FastAPI receives JSON from the frontend.

Example:

{
    "id":"101",
    "name":"Rinkesh",
    "Married":"False"
}

FastAPI internally creates

User(**request_data)

Pydantic validates and converts the values before
your business logic runs.

This prevents invalid data from reaching
your database.

==========================================================
Key Points
==========================================================

✔ BaseModel validates data.

✔ Compatible values are automatically converted.

✔ Invalid values raise ValidationError.

✔ Widely used with FastAPI, APIs,
database applications, and backend services.

==========================================================


"""