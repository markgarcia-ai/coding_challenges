"""
Challenge 33: Multithreading

Problem Statement:
Use the `threading` module to run two simple "worker" functions at the same time. Each worker will print messages with a short delay to simulate doing work, showing that their execution is interleaved.

Requirements:
- Import the `threading` and `time` modules.
- Create a worker function, e.g., `task(name, delay)`, that loops a few times, printing its name and the loop number, and sleeping for the given delay.
- In the main block, create two `Thread` objects, each targeting the `task` function but with different names and delays.
- Start both threads.
- Use the `join()` method on both threads to make the main script wait for them to finish before exiting.

Solution:
"""
import threading
import time

def task(name, delay):
    """A simple worker function for a thread."""
    print(f"Thread '{name}': starting.")
    for i in range(3):
        time.sleep(delay)
        print(f"Thread '{name}': working on step {i+1}...")
    print(f"Thread '{name}': finished.")

# Example usage:
if __name__ == "__main__":
    print("Main: creating threads.")
    # Create Thread objects
    thread1 = threading.Thread(target=task, args=("Worker-A", 1))
    thread2 = threading.Thread(target=task, args=("Worker-B", 0.7))

    # Start the threads
    print("Main: starting threads.")
    thread1.start()
    thread2.start()

    # Wait for both threads to complete
    print("Main: waiting for threads to finish.")
    thread1.join()
    thread2.join()

    print("Main: all done.")

"""
Expected Output (the order of 'working' lines may vary):

Main: creating threads.
Main: starting threads.
Thread 'Worker-A': starting.
Thread 'Worker-B': starting.
Main: waiting for threads to finish.
Thread 'Worker-B': working on step 1...
Thread 'Worker-A': working on step 1...
Thread 'Worker-B': working on step 2...
Thread 'Worker-A': working on step 2...
Thread 'Worker-B': working on step 3...
Thread 'Worker-B': finished.
Thread 'Worker-A': working on step 3...
Thread 'Worker-A': finished.
Main: all done.
""" 