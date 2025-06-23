"""
Challenge 29: Iterators

Problem Statement:
Create a custom iterator class `Countdown` that counts down from a given start number to 1. The class should be iterable, meaning you can use it in a `for` loop.

Requirements:
- Create a class named `Countdown`.
- The `__init__` constructor should take a `start` number.
- The `__iter__` method should return the iterator object itself (`self`). This makes the class an iterable.
- The `__next__` method should perform the countdown logic. It should decrease the count by one each time it's called and return the current number. When the count reaches zero, it should raise a `StopIteration` exception to signal the end of the iteration.

Solution:
"""

class Countdown:
    """A custom iterator to count down from a start number."""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        """Returns the iterator object itself."""
        return self

    def __next__(self):
        """Returns the next value in the iteration."""
        if self.current <= 0:
            # Signal that the iteration is complete.
            raise StopIteration
        else:
            # Return the current number and decrement for the next call.
            num = self.current
            self.current -= 1
            return num

# Example usage:
if __name__ == "__main__":
    print("Countdown from 5:")
    # The for loop automatically calls __iter__ once, and __next__ repeatedly.
    for number in Countdown(5):
        print(number)
        
    print("\nCountdown from 3:")
    countdown_iterator = Countdown(3)
    # You can also use the iterator manually
    try:
        print(next(countdown_iterator))
        print(next(countdown_iterator))
        print(next(countdown_iterator))
        print(next(countdown_iterator)) # This will raise StopIteration
    except StopIteration:
        print("Countdown finished.")


"""
Expected Output:

Countdown from 5:
5
4
3
2
1

Countdown from 3:
3
2
1
Countdown finished.
""" 