"""
====================================================================
      Multiprocessing Example - Reading Multiple Files
====================================================================

Real World Scenario
-------------------

Imagine a project has many log files.

logs/

    server1.log
    server2.log
    server3.log
    server4.log

Each log file contains thousands of lines.

Instead of reading them one by one,
we can let multiple CPU processes read them simultaneously.

====================================================================
"""

from multiprocessing import Process
import time


def read_log(filename):

    print(f"Started reading {filename}")

    # Simulate reading a huge file
    time.sleep(5)

    print(f"Finished reading {filename}")


if __name__ == "__main__":

    log_files = [
        "server1.log",
        "server2.log",
        "server3.log",
        "server4.log"
    ]

    processes = []

    # Create one process for each file

    for file in log_files:

        process = Process(
            target=read_log,
            args=(file,)
        )

        processes.append(process)

        process.start()

    # Wait until every process finishes

    for process in processes:
        process.join()

    print("\nAll log files processed successfully.")