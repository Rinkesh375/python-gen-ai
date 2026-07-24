"""
====================================================================
           Handling Multiple Exceptions in Python
====================================================================

Topic
-----

try
raise
ValueError
KeyError
Dictionary Lookup
Input Validation

====================================================================
Program
====================================================================

def process_order(order_type, quantity):

    try:

        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be an integer greater than 0.")

        menu = {
            "masala": 50,
            "ginger": 60,
            "elaichi": 70
        }

        price = menu[order_type]

        total = price * quantity

        print(f"{order_type.title()} price will be ₹{total}")

    except KeyError:
        print(f"{order_type} is not available in the menu.")

    except ValueError as error:
        print(error)


====================================================================
Purpose of this Program
====================================================================

Hinglish
---------

Ye program chai order process karta hai.

Sabse pehle

Quantity check karta hai.

Agar quantity galat hai

to ValueError raise karta hai.

Uske baad

Dictionary se price nikalta hai.

Agar chai ka naam dictionary me nahi hai

to KeyError aata hai.

Finally

Total price print hoti hai.

------------------------------------------------------------

English
--------

This program processes a tea order.

It first validates the quantity.

If the quantity is invalid,
it raises a ValueError.

Then it searches for the tea
inside the menu dictionary.

If the tea is missing,

Python raises a KeyError.

Otherwise,

the total price is calculated.

====================================================================
Step 1
====================================================================

def process_order(order_type, quantity):

Hinglish

Ek function banaya.

Ye do values leta hai.

1. Order Type

2. Quantity

Example

process_order("masala",3)

order_type

masala

quantity

3

------------------------------------------------------------

English

The function accepts two parameters.

order_type

quantity

====================================================================
Step 2
====================================================================

try:

Hinglish

Is block ke andar error aa sakta hai.

Isliye code try block me likha.

English

The try block contains code
that may produce an exception.

====================================================================
Step 3
====================================================================

if not isinstance(quantity,int) or quantity<=0

Hinglish

Yahan do conditions check ho rahi hain.

Condition 1

Quantity integer honi chahiye.

Condition 2

Quantity zero se badi honi chahiye.

Examples

3

✔

10

✔

0

❌

-5

❌

"five"

❌

[]

❌

------------------------------------------------------------

English

The quantity must

be an integer

and

greater than zero.

====================================================================
Step 4
====================================================================

raise ValueError(...)

Hinglish

Agar quantity galat hai

to hum khud error generate karte hain.

Python automatically error nahi de raha.

Hum manually raise kar rahe hain.

------------------------------------------------------------

English

raise manually creates
a ValueError.

====================================================================
Step 5
====================================================================

menu = {

...

}

Hinglish

Ye dictionary hai.

Tea ka naam

Key

Price

Value

Example

"masala"

↓

50

------------------------------------------------------------

English

The dictionary stores

Tea Name

↓

Price

====================================================================
Step 6
====================================================================

price = menu[order_type]

Hinglish

Python dictionary me

order_type

search karta hai.

Example

order_type

=

"masala"

Result

50

Agar

order_type

=

"coffee"

Dictionary me nahi hai.

Python

KeyError

de deta hai.

------------------------------------------------------------

English

Python searches the dictionary.

If the key exists,

its value is returned.

Otherwise,

Python raises KeyError.

====================================================================
Step 7
====================================================================

total = price * quantity

Hinglish

Total bill calculate hota hai.

Example

Price

50

Quantity

3

Total

150

------------------------------------------------------------

English

The total amount is calculated.

Formula

Price × Quantity

====================================================================
Step 8
====================================================================

except KeyError

Hinglish

Agar chai dictionary me nahi hai,

to ye block execute hoga.

Example

process_order("coffee",2)

Output

coffee is not available in the menu.

------------------------------------------------------------

English

Handles the error when

the requested key

does not exist.

====================================================================
Step 9
====================================================================

except ValueError

Hinglish

Ye invalid quantity ko handle karta hai.

Example

process_order("masala","hello")

Output

Quantity must be an integer greater than 0.

------------------------------------------------------------

English

Handles invalid quantity values.

====================================================================
Program Flow
====================================================================

Example 1

process_order("masala",3)

↓

Quantity valid

↓

Dictionary search

↓

Price = 50

↓

50 × 3

↓

150

↓

Output

Masala price will be ₹150

------------------------------------------------------------

Example 2

process_order("masa",3)

↓

Quantity valid

↓

Dictionary search

↓

Key not found

↓

KeyError

↓

except KeyError

↓

masa is not available in the menu.

------------------------------------------------------------

Example 3

process_order("masala","chunnu")

↓

Quantity check

↓

Not Integer

↓

raise ValueError

↓

except ValueError

↓

Quantity must be an integer greater than 0.

------------------------------------------------------------

Example 4

process_order("masala",-5)

↓

Negative Quantity

↓

ValueError

====================================================================
Expected Output
====================================================================

process_order("masala",3)

Masala price will be ₹150

------------------------------------------------------------

process_order("masa",3)

masa is not available in the menu.

------------------------------------------------------------

process_order("masala","chunnu")

Quantity must be an integer greater than 0.

====================================================================
Interview Questions
====================================================================

Q1

Why use raise?

Answer

To manually generate an exception.

------------------------------------------------------------

Q2

Why does KeyError occur?

Answer

Because the requested key
does not exist in the dictionary.

------------------------------------------------------------

Q3

Why check isinstance()?

Answer

To ensure the quantity
has the correct datatype.

------------------------------------------------------------

Q4

Why write multiple except blocks?

Answer

Each except block handles
a different type of exception.

====================================================================
Quick Revision
====================================================================

try
----
Code that may fail.

raise
------
Create an exception manually.

ValueError
----------
Wrong value supplied.

KeyError
---------
Dictionary key missing.

Dictionary
----------
Stores key-value pairs.

====================================================================
Golden Rule
====================================================================

✔ Validate input first.

✔ Raise meaningful exceptions.

✔ Handle specific exceptions.

✔ Write user-friendly error messages.

Never write

print("Error")

Instead write

print("Quantity must be greater than 0.")

or

print("Masala tea is not available.")

because good error messages save debugging time.

====================================================================
End of Notes
====================================================================

"""