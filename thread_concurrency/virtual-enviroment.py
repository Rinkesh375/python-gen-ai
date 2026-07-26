"""
====================================================================
        Python Virtual Environment (venv) - Git Bash Notes
====================================================================

Author : Your Python Learning Notes

====================================================================
What is a Virtual Environment?
====================================================================

Hinglish
---------

Virtual Environment (venv) ek isolated Python environment hota hai.

Iska purpose hai ki har project ke packages
alag-alag rahen.

Agar ek project me

Django 5

aur doosre project me

Django 4

ho,

to dono bina conflict ke chal sakte hain.

------------------------------------------------------------

English
--------

A Virtual Environment is an isolated Python environment.

Each project has its own

✔ Packages

✔ Dependencies

✔ Python libraries

without affecting other projects.

====================================================================
Why Should We Use venv?
====================================================================

Without Virtual Environment

Project A

↓

Flask 3.1

Project B

↓

Flask 2.3

Problem

Both projects use the same global Python packages.

Version conflicts may happen.

------------------------------------------------------------

With Virtual Environment

Project A

↓

.venv

↓

Flask 3.1

----------------------------

Project B

↓

.venv

↓

Flask 2.3

No conflicts.

Every project has its own environment.

====================================================================
Step 1
Go to Your Project Folder
====================================================================

Command

cd path/to/project

Example

cd ~/Desktop/python-gen-ai

Explanation

This opens your project folder.

====================================================================
Step 2
Create Virtual Environment
====================================================================

Command

python -m venv .venv

Explanation

python

↓

Runs Python

------------------------------------------------------------

-m

Means

Run a Python module.

------------------------------------------------------------

venv

Python's built-in module
for creating virtual environments.

------------------------------------------------------------

.venv

Name of the virtual environment folder.

After running,

your project becomes

python-gen-ai/

│

├── .venv/

├── app.py

└── requirements.txt

====================================================================
Step 3
Activate Virtual Environment (Git Bash)
====================================================================

Command

source .venv/Scripts/activate

Explanation

source

↓

Runs the activation script
inside the current terminal.

After activation,

your terminal becomes

(.venv)

user@PC

$

This means

Virtual Environment is ACTIVE.

====================================================================
Step 4
Check Installed Packages
====================================================================

Command

pip list

Explanation

Shows all installed packages
inside the current virtual environment.

Example

Package

Version

-----------

pip

25.x.x

setuptools

80.x.x

====================================================================
Step 5
Install Packages
====================================================================

Command

pip install requests

or

pip install flask

or

pip install pandas

Explanation

Installs packages only
inside the current virtual environment.

Other projects are NOT affected.

====================================================================
Step 6
Save Installed Packages
====================================================================

Command

pip freeze > requirements.txt

Explanation

Creates

requirements.txt

containing all installed packages.

Example

requests==2.32.5

pandas==2.3.1

numpy==2.3.2

This file is shared with other developers.

====================================================================
Step 7
Install Packages From requirements.txt
====================================================================

Command

pip install -r requirements.txt

Explanation

Reads every package from

requirements.txt

and installs them automatically.

Useful when cloning a Git project.

====================================================================
Step 8
Deactivate Virtual Environment
====================================================================

Command

deactivate

Explanation

Exits the virtual environment.

Your terminal changes from

(.venv)

↓

user@PC $

Now Python returns to the global installation.

====================================================================
Complete Workflow
====================================================================

# Go to project

cd ~/Desktop/python-gen-ai

------------------------------------------------------------

# Create virtual environment

python -m venv .venv

------------------------------------------------------------

# Activate (Git Bash)

source .venv/Scripts/activate

------------------------------------------------------------

# Install packages

pip install requests

------------------------------------------------------------

# Verify packages

pip list

------------------------------------------------------------

# Save dependencies

pip freeze > requirements.txt

------------------------------------------------------------

# Exit virtual environment

deactivate

====================================================================
Folder Structure
====================================================================

python-gen-ai/

│

├── .venv/

│     ├── Scripts/

│     ├── Lib/

│     ├── Include/

│     └── pyvenv.cfg

│

├── app.py

├── requirements.txt

└── README.md

====================================================================
Common Commands
====================================================================

Create venv

python -m venv .venv

--------------------------------

Activate (Git Bash)

source .venv/Scripts/activate

--------------------------------

Install package

pip install package_name

--------------------------------

Show packages

pip list

--------------------------------

Save packages

pip freeze > requirements.txt

--------------------------------

Install from requirements

pip install -r requirements.txt

--------------------------------

Deactivate

deactivate

====================================================================
Best Practices
====================================================================

✔ Create one virtual environment per project.

✔ Name it ".venv" (recommended).

✔ Never upload the ".venv" folder to GitHub.

✔ Add ".venv/" to your ".gitignore" file.

✔ Commit "requirements.txt" so others can install the same packages.

====================================================================
Real-World Workflow
====================================================================

Clone Project

↓

cd project

↓

python -m venv .venv

↓

source .venv/Scripts/activate

↓

pip install -r requirements.txt

↓

Start Coding

====================================================================
Golden Rule
====================================================================

Every New Python Project

↓

Create Virtual Environment

↓

Activate It

↓

Install Packages

↓

Save requirements.txt

↓

Deactivate When Finished

====================================================================
End of Notes
====================================================================


"""