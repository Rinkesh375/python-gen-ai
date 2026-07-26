"""
===========================================================
        Why do we need

        if __name__ == "__main__"

===========================================================

Problem
-------

When using multiprocessing,

Python creates a NEW process.

That new process imports the same file again.

Without protection,

the imported file creates more processes,

which import the file again,

creating an infinite loop.

-----------------------------------------------------------

Wrong

process.start()

↓

Child imports file

↓

process.start()

↓

Child imports file

↓

∞

-----------------------------------------------------------

Correct

if __name__ == "__main__":

    process.start()

Now

Only the original program
creates new processes.

Child processes only execute
their assigned target function.

-----------------------------------------------------------

Why Threading doesn't need it

Threads

✔ Same Process

✔ Shared Memory

✔ No re-import

Processes

✔ New Python Process

✔ Imports file again

✔ Needs protection

-----------------------------------------------------------

Golden Rule

Whenever you use

multiprocessing.Process()

always write

if __name__ == "__main__":

===========================================================
"""