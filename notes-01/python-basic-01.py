"""
JavaScript (Node.js) vs Python

------------------------------------------------------------
JavaScript (Node.js)              | Python
------------------------------------------------------------
package.json                      | requirements.txt / pyproject.toml
npm install                       | pip install
node_modules                      | venv + site-packages
npm install axios                 | pip install requests
package-lock.json                 | requirements.txt (generated using pip freeze)
nvm (Node Version Manager)        | pyenv (Python Version Manager)
------------------------------------------------------------

Important Note:

❌ node_modules = venv

✅ node_modules = site-packages (inside venv)

Directory Structure:

JavaScript:

project/
│
├── package.json
└── node_modules/

Python:

project/
│
├── requirements.txt
└── venv/
    └── Lib/
        └── site-packages/

Memory Trick:

JavaScript:
package.json
    ↓
npm install
    ↓
node_modules

Python:
requirements.txt
    ↓
pip install
    ↓
venv/site-packages

Summary:

- package.json is similar to requirements.txt.
- npm install is similar to pip install.
- node_modules stores installed JavaScript packages.
- site-packages stores installed Python packages.
- venv creates an isolated environment for a Python project.
- pyenv manages Python versions, similar to nvm for Node.js.
"""





"""

How to Create Virtual Environment
python -m venv venv

python     → Python interpreter

-m         → Run module

venv       → Virtual environment module

venv       → Folder name

"""








"""
Activate Virtual Environment

powershell
venv\Scripts\activate
(venv) C:\Users\Rinkesh\myproject>



bash

source venv/Scripts/activate


to verify use this

write this command it will show the 
which python


example
rinke@Rinkesh MINGW64 ~/Desktop/python-gen-ai/virtual-enviroment-01 (main)
$ which python
/c/Users/rinke/Desktop/python-gen-ai/virtual-enviroment-01/venv/Scripts/python
(venv) 
"""



"""

pip install -r requirement.txt

"""



"""

what does this deactivate command do


DEACTIVATE COMMAND

Command:
    deactivate

Purpose:
    Exit the currently active virtual environment.

Before:
    (venv) $

After:
    $

What it does:
    1. Removes virtual environment settings.
    2. Restores original system PATH.
    3. Switches Python back to global installation.
    4. Switches pip back to global installation.

Use Case:
    Run when you are done working in a virtual environment.

Key Point:
    deactivate does NOT delete the venv.
    It only exits the active virtual environment.


"""


