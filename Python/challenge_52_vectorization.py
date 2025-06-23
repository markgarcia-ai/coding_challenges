"""
Challenge 52: Vectorization with NumPy

Problem Statement:
Demonstrate the performance difference between a standard Python loop and a vectorized NumPy operation for adding two large lists of numbers.

Requirements:
- You will need the `numpy` library (`pip install numpy`).
- Create two large Python lists of numbers (e.g., 1 million numbers each).
- **Method 1 (Loop):** Write a function that takes the two lists and adds them element by element using a `for` loop, returning a new list. Time how long this takes.
- **Method 2 (Vectorized):** Convert the lists to NumPy arrays. Add the arrays together with a single `+` operation. Time how long this takes.
- Print both timings to show the speed advantage of vectorization.

Solution:
"""
import numpy as np
import time

def add_with_loop(list1, list2):
    """Adds two lists element-wise using a Python for loop."""
    result_list = []
    for i in range(len(list1)):
        result_list.append(list1[i] + list2[i])
    return result_list

def add_with_numpy(arr1, arr2):
    """Adds two NumPy arrays using a single vectorized operation."""
    return arr1 + arr2

# Example usage:
if __name__ == "__main__":
    # Setup
    list_size = 1_000_000
    list_a = list(range(list_size))
    list_b = list(range(list_size))
    
    # --- Method 1: Standard Python Loop ---
    start_time_loop = time.time()
    result_loop = add_with_loop(list_a, list_b)
    end_time_loop = time.time()
    loop_duration = end_time_loop - start_time_loop
    print(f"Time taken with Python loop: {loop_duration:.6f} seconds.")
    
    # --- Method 2: Vectorized NumPy Operation ---
    arr_a = np.array(list_a)
    arr_b = np.array(list_b)
    
    start_time_numpy = time.time()
    result_numpy = add_with_numpy(arr_a, arr_b)
    end_time_numpy = time.time()
    numpy_duration = end_time_numpy - start_time_numpy
    print(f"Time taken with NumPy vectorization: {numpy_duration:.6f} seconds.")
    
    print(f"\nNumPy was approximately {loop_duration / numpy_duration:.1f}x faster.")

"""
Expected Output (exact times will vary, but the difference should be significant):

Time taken with Python loop: 0.123456 seconds.
Time taken with NumPy vectorization: 0.001234 seconds.

NumPy was approximately 100.0x faster.
""" 