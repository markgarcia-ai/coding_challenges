"""
Challenge 56: `datetime` module

Problem Statement:
Use the `datetime` module to perform three common date and time operations:
1.  Get the current date and time.
2.  Format a `datetime` object into a custom string.
3.  Calculate a future date by adding a `timedelta`.

Requirements:
- Import the `datetime` and `timedelta` objects from the `datetime` module.
- **Task 1**: Get the current local date and time using `datetime.now()` and print it.
- **Task 2**: Format the current `datetime` object into a more readable string, like "Month Day, Year - HH:MM:SS".
- **Task 3**: Create a `timedelta` object representing 10 days and add it to the current date to find the date 10 days from now.

Solution:
"""
from datetime import datetime, timedelta

# Example usage:
if __name__ == "__main__":
    # Task 1: Get the current date and time
    now = datetime.now()
    print(f"1. Current date and time: {now}")

    # Task 2: Format the datetime object into a string
    # %B: Full month name, %d: Day of the month, %Y: Full year
    # %H: Hour (24h), %M: Minute, %S: Second
    formatted_string = now.strftime("%B %d, %Y - %H:%M:%S")
    print(f"2. Formatted string: {formatted_string}")

    # Task 3: Calculate a future date
    ten_days = timedelta(days=10)
    future_date = now + ten_days
    print(f"3. Current date is {now.strftime('%Y-%m-%d')}")
    print(f"   Date in 10 days will be: {future_date.strftime('%Y-%m-%d')}")

"""
Expected Output (dates and times will match when you run it):

1. Current date and time: 2023-10-27 11:05:30.123456
2. Formatted string: October 27, 2023 - 11:05:30
3. Current date is 2023-10-27
   Date in 10 days will be: 2023-11-06
""" 