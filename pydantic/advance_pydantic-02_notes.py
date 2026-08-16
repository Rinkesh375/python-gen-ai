"""
=========================================================
Topic : Pydantic Default Field Value
File  : pydantic_default_field_notes.py
=========================================================

CODE

class TextContent(BaseModel):
    type: str = "text"
    content: str

---------------------------------------------------------

YEH CLASS KYA HAI?

Socho Class ek Blueprint ya Form hai.

Jaise School Admission Form mein fields hoti hain

Name
Age
Class

Waise hi TextContent mein 2 fields hain

type
content

Har baar jab hum TextContent object banayenge,
yeh dono fields available hongi.

---------------------------------------------------------

type: str = "text"

Is line ko 3 parts mein samjho.

1.

type

Ye field ka naam hai.

Jaise

name

age

email

waise hi

type

---------------------------------------------------------

2.

: str

Matlab

Is field mein sirf String value aani chahiye.

Sahi

"text"

"image"

Galat

100

True

[]

---------------------------------------------------------

3.

= "text"

Ye DEFAULT VALUE hai.

Matlab

Agar user type nahi dega

to Pydantic automatically

type="text"

bhar dega.

Example

Input

TextContent(
    content="Hello World"
)

Pydantic internally bana dega

TextContent(
    type="text",
    content="Hello World"
)

---------------------------------------------------------

content: str

Ye actual text store karega.

Example

"Python Easy Hai"

"Hello World"

---------------------------------------------------------

OBJECT BANATE TIME

text = TextContent(
    content="Hello World"
)

Humne sirf content diya.

type nahi diya.

Fir bhi object ban gaya.

Kyun?

Kyuki default value

"text"

already set thi.

---------------------------------------------------------

OUTPUT

type='text'

content='Hello World'

---------------------------------------------------------

REAL LIFE EXAMPLE

WhatsApp Message

{
   "type":"text",
   "message":"Hello"
}

Photo Message

{
   "type":"image",
   "url":"cat.png"
}

Yahan "type" app ko batata hai
ki ye kis type ka message hai.

---------------------------------------------------------

IMPORTANT

Bahut log sochte hain

type: str = "text"

matlab sirf "text" hi allowed hai.

❌ Galat

Iska matlab sirf itna hai

Default value "text" hai.

Agar tum manually likho

TextContent(
    type="image",
    content="Hello"
)

To ye chal jayega.

Kyun?

Kyuki "image" bhi ek String hai.

---------------------------------------------------------

BEST PRACTICE

Instead of

type: str = "text"

Use

type: Literal["text"] = "text"

Ab sirf

"text"

hi allowed hoga.

Agar koi

type="image"

dega

ValidationError aa jayega.

---------------------------------------------------------

1 Minute Revision

✔ BaseModel -> Validation deta hai

✔ type -> Field Name

✔ str -> Data Type

✔ "text" -> Default Value

✔ content -> Required Field

✔ Default value automatically fill hoti hai.

✔ Better Practice

Literal["text"]

=========================================================
"""