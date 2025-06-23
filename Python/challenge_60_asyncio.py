"""
Challenge 60: `asyncio` for Asynchronous Programming

Problem Statement:
Use the `asyncio` module to run two asynchronous "tasks" concurrently. The tasks will simulate I/O operations (like waiting for a web request) by using `asyncio.sleep()`. This demonstrates how `asyncio` can perform other work while one task is "waiting".

Requirements:
- Import the `asyncio` and `datetime` modules.
- Create an asynchronous function `fetch_data(name, delay)` using the `async def` syntax.
- Inside the function, it should print a "start" message, then use `await asyncio.sleep(delay)` to simulate a non-blocking wait, and finally print an "end" message.
- Create a main asynchronous function `main()` that creates and runs two `fetch_data` tasks concurrently using `asyncio.gather()`.
- Run the `main` function using `asyncio.run()`.

Solution:
"""
import asyncio
import datetime

def print_now(msg):
    """Helper function to print messages with a timestamp."""
    ts = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"[{ts}] {msg}")

async def fetch_data(name, delay):
    """A coroutine that simulates fetching data with a delay."""
    print_now(f"Task '{name}' started, will wait for {delay} second(s).")
    await asyncio.sleep(delay)
    print_now(f"Task '{name}' finished.")
    return f"Data from {name}"

async def main():
    """The main coroutine to orchestrate the tasks."""
    print_now("Starting main program...")
    
    # asyncio.gather() runs the tasks concurrently and waits for them all to finish.
    results = await asyncio.gather(
        fetch_data("A", 2),
        fetch_data("B", 1)
    )
    
    print_now(f"All tasks completed. Results: {results}")

# Example usage:
if __name__ == "__main__":
    # asyncio.run() starts the event loop and runs the main coroutine.
    asyncio.run(main())

"""
Expected Output (timestamps will show concurrent execution):

[12:00:00.000] Starting main program...
[12:00:00.001] Task 'A' started, will wait for 2 second(s).
[12:00:00.002] Task 'B' started, will wait for 1 second(s).
[12:00:01.003] Task 'B' finished.
[12:00:02.002] Task 'A' finished.
[12:00:02.003] All tasks completed. Results: ['Data from A', 'Data from B']
""" 