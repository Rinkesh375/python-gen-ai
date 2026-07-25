"""
====================================================================
            Real-Time Example of Multithreading
====================================================================

Project
-------
Sending emails to multiple users.

Why use Threads?
----------------

Imagine you have 5 users.

Sending one email takes 2 seconds.

Without Threads

User 1 → 2 sec

↓

User 2 → 2 sec

↓

User 3 → 2 sec

↓

User 4 → 2 sec

↓

User 5 → 2 sec

Total = 10 seconds

------------------------------------------------------------

With Threads

All emails start together.

Total ≈ 2 seconds

This is why multithreading is useful.

====================================================================
"""

import threading
import time


def send_email(user):

    print(f"Sending email to {user}...")

    # Simulate sending email
    time.sleep(2)

    print(f"Email sent to {user}")


users = [
    "Rinkesh",
    "Rahul",
    "Amit",
    "Neha",
    "Priya"
]


threads = []


for user in users:

    thread = threading.Thread(target=send_email, args=(user,))

    threads.append(thread)

    thread.start()


# Wait for every email to finish

for thread in threads:
    thread.join()


print("\nAll emails have been sent.")