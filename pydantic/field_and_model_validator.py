"""
==========================================================
File Name : field_and_model_validator.py

Topic :
    Pydantic V2
    - field_validator
    - model_validator
    - EmailStr
    - Field
    - mode="before"
    - mode="after"

Author Notes:
    These notes are written in Hinglish + English
    for interview preparation and future revision.
==========================================================
"""

# --------------------------------------------
# IMPORTS
# --------------------------------------------

from pydantic import BaseModel, field_validator, model_validator, EmailStr, Field
from datetime import datetime

# ==========================================================
# BaseModel
# ==========================================================
#
# BaseModel is the parent class of every Pydantic model.
#
# Think of it as:
#
# Normal Python Class
#        ❌ No validation
#
# BaseModel
#        ✅ Automatic validation
#        ✅ Type conversion
#        ✅ Better error messages
#
# Real Life Example:
#
# User Registration Form
#
# Instead of checking every field manually,
# BaseModel validates everything automatically.
#
# Interview Question:
# Q. Why do we inherit from BaseModel?
#
# Answer:
# Because it provides automatic data validation,
# parsing, serialization and error handling.
#
# ==========================================================



class Person(BaseModel):

    # -----------------------------------------
    # firstName
    #
    # Expected Type:
    # str
    #
    # Example:
    #
    # Good
    # ------
    # Rinkesh
    #
    # Bad
    # -----
    # rinkesh
    #
    # -----------------------------------------

    firstName: str

    # -----------------------------------------
    # lastName
    # -----------------------------------------

    lastName: str


    # =====================================================
    # field_validator
    #
    # Runs for:
    #
    # firstName
    # lastName
    #
    # Because both fields need same validation.
    #
    # =====================================================

    @field_validator("firstName", "lastName")
    @classmethod
    def check_name_capitalization(cls, value):

        # istitle() returns True if
        #
        # Every word starts with Capital Letter.
        #
        # Example:
        #
        # "Rinkesh"      True
        # "Kumar"        True
        # "rinkesh"      False
        # "RINKESH"      False
        #

        if not value.istitle():

            raise ValueError(
                "First character must be capital."
            )

        return value


# =====================================================
# GOOD INPUT
#
# Person(
#     firstName="Rinkesh",
#     lastName="Kumar"
# )
#
# OUTPUT
#
# firstName='Rinkesh'
# lastName='Kumar'
#
# =====================================================

# =====================================================
# BAD INPUT
#
# Person(
#     firstName="rinkesh",
#     lastName="Kumar"
# )
#
# OUTPUT
#
# ValidationError
#
# =====================================================


# =====================================================
# Real World Use
#
# ✔ HR Software
# ✔ School Admission
# ✔ Banking
# ✔ Passport Portal
#
# =====================================================