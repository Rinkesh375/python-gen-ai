"""
==========================================================
Topic : Pydantic Field Validator & Model Validator
File  : pydantic_field_and_model_validators.py
==========================================================

Required Package
----------------

pip install pydantic

==========================================================
Code
==========================================================

from pydantic import BaseModel, field_validator, model_validator


class User_name(BaseModel):
    user_name: str

    @field_validator("user_name")
    @classmethod
    def username_length_checker(cls, value):
        if len(value) < 1:
            raise ValueError(
                "user_name must be greater than equal to 1 character"
            )
        return value


class Password(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def password_matcher(self):
        if self.password != self.confirm_password:
            raise ValueError(
                "password and confirm password must be same"
            )
        return self


print(
    Password(
        password="124",
        confirm_password="1245"
    )
)

==========================================================
1. Hinglish Explanation
==========================================================

Pydantic me do tarah ke validation bahut common hain.

1.

field_validator()

Ek field ko validate karta hai.

2.

model_validator()

Multiple fields ko ek sath validate karta hai.

----------------------------------------------------------
field_validator
----------------------------------------------------------

class User_name(BaseModel):

    user_name:str

Yaha sirf ek field hai.

user_name

Ab hum check karna chahte hain ki

username empty na ho.

Isliye

@field_validator("user_name")

lagaya gaya hai.

Ye validator

sirf

user_name

field ke liye chalega.

----------------------------------------------------------

@field_validator("user_name")

@classmethod

def username_length_checker(cls,value):

Yaha

value

me

user_name

ki value aati hai.

Example

User_name(

user_name="Rinkesh"

)

value

↓

"Rinkesh"

----------------------------------------------------------

if len(value) < 1

Agar

length

1 se kam hai.

Example

""

↓

Length

0

↓

ValidationError

----------------------------------------------------------

return value

Validation successful hone ke baad

value return karni padti hai.

Agar return nahi karoge

to Pydantic

None

assign kar dega.

==========================================================
Example 1
==========================================================

User_name(

user_name="Rinkesh"

)

Validation

↓

Length

7

↓

Pass

Output

User_name(user_name='Rinkesh')

==========================================================
Example 2
==========================================================

User_name(

user_name=""

)

Validation

↓

Length

0

↓

ValidationError

==========================================================
model_validator
==========================================================

Field validator

ek field check karta hai.

Model validator

multiple fields ko compare karta hai.

Example

password

confirm_password

Ye dono alag fields hain.

Agar dono same nahi hain

to account create nahi hona chahiye.

==========================================================

@model_validator(mode="after")

def password_matcher(self):

Ye validator

tab chalega

jab

password

aur

confirm_password

dono fields pehle validate ho chuki hongi.

Isliye

mode="after"

likha gaya hai.

==========================================================

if self.password != self.confirm_password

Example

password

↓

1234

confirm_password

↓

12345

Equal nahi hain.

↓

ValidationError

==========================================================

return self

Model validator me

poora object

return karte hain.

==========================================================
Your Example
==========================================================

Password(

password="124",

confirm_password="1245"

)

Validation

↓

124

!=

1245

↓

ValidationError

Output

password and confirm password must be same

==========================================================
Real World Example 1
==========================================================

Signup Form

Frontend

↓

Password

↓

Confirm Password

Backend

↓

Compare both values

↓

Create account

Ye almost har website karti hai.

==========================================================
Real World Example 2
==========================================================

Bank Account

withdraw_amount

balance

Model validator

check karega

withdraw_amount

>

balance

↓

Error

==========================================================
Real World Example 3
==========================================================

Hotel Booking

check_in

check_out

Model validator

check karega

check_out

>

check_in

==========================================================
Real World Example 4
==========================================================

Discount

price

discount

Discount

kabhi bhi

price

se zyada nahi ho sakta.

==========================================================
Bad Examples
==========================================================

❌

User_name(

user_name=""

)

Reason

Username empty hai.

----------------------------------------------------------

❌

Password(

password="abcd",

confirm_password="xyz"

)

Reason

Password match nahi kar raha.

----------------------------------------------------------

❌

Password(

password="123456",

confirm_password="12345"

)

Reason

Length same hona zaruri nahi.

Actual value same honi chahiye.

==========================================================
Quick Revision
==========================================================

field_validator

↓

Single Field Validation

--------------------------

model_validator

↓

Multiple Fields Validation

==========================================================



==========================================================
2. English Explanation
==========================================================

Pydantic provides two major validators.

1.

field_validator()

Validates a single field.

2.

model_validator()

Validates the entire model or compares multiple fields.

==========================================================
field_validator
==========================================================

class User_name(BaseModel):

    user_name:str

This model contains one field.

The validator

@field_validator("user_name")

runs only for

user_name.

The input value is received in

value.

Example

User_name(

user_name="Rinkesh"

)

value

↓

"Rinkesh"

==========================================================

if len(value) < 1

If the username length is less than one,

raise

ValidationError.

==========================================================

return value

Always return the validated value.

==========================================================
model_validator
==========================================================

Model validators work with multiple fields.

Example

password

confirm_password

Both fields should contain exactly the same value.

==========================================================

mode="after"

means

Run this validator only after all individual field
validations have completed successfully.

==========================================================

if self.password != self.confirm_password

Raise

ValidationError.

==========================================================
Output
==========================================================

Password(

password="124",

confirm_password="1245"

)

↓

ValidationError

password and confirm password must be same

==========================================================
Production Examples
==========================================================

✔ User Registration

Compare

password

confirm_password

--------------------------------

✔ Hotel Booking

check_in

must be before

check_out

--------------------------------

✔ Banking

withdraw

cannot exceed

balance

--------------------------------

✔ E-commerce

discount

cannot exceed

price

==========================================================

"""