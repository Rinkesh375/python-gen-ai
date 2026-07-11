"""
==========================================================
Summary: Why Was the Import Error Happening?
==========================================================

Error 1
-------

ImportError:
attempted relative import with no known parent package

Why?

We wrote:

from .recipes.flavours import ginger_chai

The '.' (dot) means:

    "Start searching from the current package."

But we executed:

python main.py

When Python runs a file directly, it treats it as a
standalone script, NOT as part of a package.

So Python does not know:

• Which package am I inside?
• Where is my parent package?

Therefore, the relative import (.) fails.

----------------------------------------------------------
How to Fix It
----------------------------------------------------------

Option 1 (Recommended for Beginners)

Use an Absolute Import:

from recipes.flavours import ginger_chai

Run:

python main.py

✔ Works because Python searches from the project folder.

----------------------------------------------------------

Option 2 (Use Relative Imports)

Keep the relative import:

from .recipes.flavours import ginger_chai

But run the file as a module:

python -m app.main

(or whatever your package name is)

✔ Now Python knows the parent package.

==========================================================
Error 2
==========================================================

ModuleNotFoundError:
No module named 'import'

Why?

We executed:

python -m import.main.py

There were TWO mistakes.

----------------------------------------------------------
Mistake 1
----------------------------------------------------------

With '-m', Python expects a MODULE NAME,
not a filename.

Wrong

python -m import.main.py

Correct

python -m import.main

Notice:
No ".py"

----------------------------------------------------------
Mistake 2
----------------------------------------------------------

We were already inside the "import" folder.

Current Location:

python-gen-ai/import/

Then we ran:

python -m import.main

Python searched for:

import/
    import/

because it always starts searching from the
CURRENT directory.

There is no second "import" folder,
so Python reported:

ModuleNotFoundError:
No module named 'import'

----------------------------------------------------------
How to Fix It
----------------------------------------------------------

Go to the parent directory first.

Example:

cd ..

Now you are here:

python-gen-ai/

Then run:

python -m import.main

Now Python can find:

python-gen-ai/
    import/
        main.py

==========================================================
Important Rules
==========================================================

Rule 1

python main.py

→ Runs a FILE.

Use Absolute Imports.

----------------------------------------------------------

Rule 2

python -m package.module

→ Runs a MODULE inside a package.

Relative Imports (.) work here.

----------------------------------------------------------

Rule 3

Never add ".py" after '-m'.

Wrong

python -m app.main.py

Correct

python -m app.main

----------------------------------------------------------

Rule 4

Run '-m' from the PARENT directory
of the package, not from inside the package.

==========================================================
Golden Formula
==========================================================

Run a file

python main.py

↓

Use

from recipes.flavours import ginger_chai

----------------------------------------------------------

Run a package

python -m app.main

↓

Use

from .recipes.flavours import ginger_chai

==========================================================
Easy Way to Remember
==========================================================

python main.py

= Standalone Script
= No Parent Package
= Relative Imports (.) ❌
= Absolute Imports ✔

------------------------------------------

python -m package.module

= Package Execution
= Parent Package Exists ✔
= Relative Imports (.) ✔
= Absolute Imports ✔

==========================================================


"""