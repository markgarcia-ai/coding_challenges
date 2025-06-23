"""
Challenge 46: `with` statement (Context Managers)

Problem Statement:
The `with` statement simplifies resource management by ensuring that resources are properly cleaned up. Create a simple class that acts as a context manager to time a block of code.

Requirements:
- Create a class `CodeTimer`.
- Implement the `__enter__` method. This method should record the start time and print a message. It is called when the `with` block is entered.
- Implement the `__exit__` method. This method takes three arguments (`exc_type`, `exc_val`, `exc_tb`) and is called when the `with` block is exited. It should calculate the elapsed time and print it.
- Use this context manager to time a simple operation, like a loop or a `time.sleep()`.

Solution:
"""
import time

class CodeTimer:
    """A context manager to time a block of code."""
    def __enter__(self):
        """Called when entering the 'with' block."""
        self.start_time = time.time()
        print("Timer started.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Called when exiting the 'with' block."""
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Block executed in: {elapsed_time:.4f} seconds.")
        # Return False to propagate exceptions, True to suppress them.
        return False

# Example usage:
if __name__ == "__main__":
    print("Preparing to run a timed block of code...")
    
    # The `with` statement creates a CodeTimer instance.
    # It automatically calls __enter__ at the start and __exit__ at the end.
    with CodeTimer():
        # This is the block of code we want to time
        print("  Inside the with block, sleeping for 1 second...")
        time.sleep(1)
        print("  ...finished sleeping.")
        
    print("The timed block has finished.")

"""
Expected Output:

Preparing to run a timed block of code...
Timer started.
  Inside the with block, sleeping for 1 second...
  ...finished sleeping.
Block executed in: 1.00XX seconds.
The timed block has finished.
""" 