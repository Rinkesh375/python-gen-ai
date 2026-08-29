"""
NOTES: export PATH and hash -r
==============================

Ye commands Git Bash me virtual environment (.venv) ke Python
ko priority dene ke liye useful hain.


------------------------------------------------------------
1. export PATH="$(pwd)/.venv/Scripts:$PATH"
------------------------------------------------------------

Simple Hinglish:

Is command ka matlab hai:

"Current project ke .venv/Scripts folder ko PATH ke sabse
aage add karo, taaki terminal sabse pehle yahin Python ko dhunde."


BREAKDOWN:

export
------
Terminal ki environment variable ki value set/change karta hai.


PATH
----
PATH ek folders ki list hoti hai jahan terminal commands
jaise python aur pip ko dhundhta hai.


$(pwd)
-------
pwd = Print Working Directory

Ye current folder ka path deta hai.

Example:

/c/Users/rinke/Desktop/python-gen-ai/gen-ai-start


$(pwd)/.venv/Scripts
--------------------
Current project ke virtual environment ka Scripts folder.

Example:

/c/Users/rinke/Desktop/python-gen-ai/gen-ai-start/.venv/Scripts


:$PATH
------
Purani PATH list ko bhi rakhta hai.

Important:

.venv/Scripts ko $PATH ke AAGE rakhne ka reason ye hai ki
terminal pehle virtual environment ke Python ko dhundhe.


Example:

BEFORE:

python
  |
  ↓
Global Python
Python314


AFTER:

python
  |
  ↓
.venv/Scripts/python     ← PEHLE YAHAN CHECK HOGA
  |
  ↓
Global Python            ← Agar upar nahi mila tab


Check karne ke liye:

which python

Expected:

/.../gen-ai-start/.venv/Scripts/python



------------------------------------------------------------
2. hash -r
------------------------------------------------------------

Simple Hinglish:

Terminal kabhi-kabhi commands ki location yaad (cache) kar
leta hai.

Example:

python → Global Python

Agar hum PATH change kar dein, terminal ke paas Python ki
purani location ki memory ho sakti hai.


hash -r

Terminal ko bolta hai:

"Commands ki purani cached locations bhool jao aur dobara
PATH me search karo."


Example:

Pehle:

python → Global Python


PATH change kiya:

export PATH="$(pwd)/.venv/Scripts:$PATH"


Phir:

hash -r


Ab terminal dobara Python ko PATH me search karega:

python → .venv/Scripts/python



IMPORTANT:

hash -r Python cache clear NAHI karta.

hash -r .venv delete NAHI karta.

hash -r Python reinstall NAHI karta.

Ye sirf shell ki command-location cache clear karta hai.



------------------------------------------------------------
3. Dono commands together
------------------------------------------------------------

export PATH="$(pwd)/.venv/Scripts:$PATH"

hash -r


Meaning:

Step 1:
.venv/Scripts ko PATH ke front me add karo.


Step 2:
Terminal ki purani command-location memory clear karo.


Step 3:
Ab "python" run karne par .venv wala Python priority
me milega.



------------------------------------------------------------
4. Verification
------------------------------------------------------------

Check karo ki kaunsa Python use ho raha hai:

which python


Expected:

/.../gen-ai-start/.venv/Scripts/python


Actual Python executable check karne ke liye:

python -c "import sys; print(sys.executable)"


Ye Python executable ka actual path print karega.



------------------------------------------------------------
5. Easy Memory Trick
------------------------------------------------------------

export PATH
------------
"Is folder ko command dhundhne ki list me priority do."


hash -r
--------
"Terminal ki purani command-location memory clear karo."


Short version:

export PATH
    ↓
.venv ko priority do

hash -r
    ↓
Purani command location bhulao


------------------------------------------------------------
6. Real Example From This Project
------------------------------------------------------------

Global Python:

/c/Users/rinke/AppData/Local/Programs/Python/Python314/python


Virtual Environment Python:

/c/Users/rinke/Desktop/python-gen-ai/gen-ai-start/.venv/Scripts/python


Command:

export PATH="$(pwd)/.venv/Scripts:$PATH"

Isse .venv/Scripts PATH ke sabse aage aa gaya.


Then:

hash -r

Isse terminal ne Python ki purani location ki cached memory
clear kar di.


Then:

which python

Output:

/c/Users/rinke/Desktop/python-gen-ai/gen-ai-start/.venv/Scripts/python


Matlab:

AB PROJECT KA VIRTUAL ENVIRONMENT WALA PYTHON USE HO RAHA HAI. ✅
"""