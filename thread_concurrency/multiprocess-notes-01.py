"""
===========================================================
            Multiprocessing in Python
===========================================================

What is Multiprocessing?

Hinglish
---------

Multiprocessing creates multiple Python processes.

Each process has its own memory.

English
--------

Multiprocessing runs multiple independent
Python processes.

-----------------------------------------------------------

Process
--------

Heavyweight

Separate memory

Used for CPU-intensive tasks.

-----------------------------------------------------------

Thread
-------

Lightweight

Shared memory

Used for I/O tasks.

-----------------------------------------------------------

Process()

Creates a new process.

-----------------------------------------------------------

target

Function to execute.

-----------------------------------------------------------

args

Arguments passed to the function.

-----------------------------------------------------------

start()

Starts the process.

-----------------------------------------------------------

join()

Waits until the process finishes.

-----------------------------------------------------------

if __name__ == "__main__"

Runs code only when the file is executed directly.

This is required when using multiprocessing.

===========================================================

Golden Rule

Process()

↓

start()

↓

join()

Always protect multiprocessing code with

if __name__ == "__main__":

===========================================================
"""