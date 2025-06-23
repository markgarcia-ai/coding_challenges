"""
Challenge 61: `multiprocessing` for Parallel CPU Work

Problem Statement:
Use the `multiprocessing` module to run two CPU-intensive tasks in parallel on different processor cores. This will demonstrate true parallelism, which is different from the concurrency model of `threading` or `asyncio`.

Requirements:
- Import the `multiprocessing` and `time` modules.
- Create a worker function, `cpu_task(name)`, that simulates a CPU-bound task by running a large loop (e.g., summing numbers up to a high value).
- The function should print when it starts and when it finishes.
- In the `if __name__ == '__main__':` block (which is required for `multiprocessing`), create two `Process` objects targeting the `cpu_task` function.
- Start both processes using `.start()`.
- Use the `.join()` method on both processes to make the main script wait for them to finish.

Solution:
"""
import multiprocessing
import time

def cpu_task(name):
    """A function that simulates a CPU-intensive task."""
    print(f"Process '{name}': starting.")
    # This loop is a simple way to make the CPU do work
    count = 0
    for i in range(100_000_000):
        count += i
    print(f"Process '{name}': finished.")

# Example usage:
if __name__ == '__main__':
    # This check is crucial for multiprocessing to work correctly on all platforms.
    
    start_time = time.time()
    
    print("Main: creating processes.")
    p1 = multiprocessing.Process(target=cpu_task, args=("CPU-Task-1",))
    p2 = multiprocessing.Process(target=cpu_task, args=("CPU-Task-2",))

    print("Main: starting processes.")
    p1.start()
    p2.start()

    print("Main: waiting for processes to finish.")
    p1.join()
    p2.join()

    end_time = time.time()
    print(f"Main: all done in {end_time - start_time:.2f} seconds.")

"""
Expected Output:

Main: creating processes.
Main: starting processes.
Process 'CPU-Task-1': starting.
Process 'CPU-Task-2': starting.
Main: waiting for processes to finish.
Process 'CPU-Task-1': finished.
Process 'CPU-Task-2': finished.
Main: all done in X.XX seconds.

(Note: The total time should be roughly the time it takes for ONE task to run,
not the sum of both, if you have at least two CPU cores).
""" 