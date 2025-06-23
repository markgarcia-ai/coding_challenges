"""
Challenge 55: `zip()` function

Problem Statement:
Use the `zip()` function to iterate over two lists simultaneously. `zip()` takes iterables and aggregates them in a tuple, which you can then use.

Requirements:
- Create two lists: one with student names and another with their corresponding scores.
- Use a `for` loop with `zip()` to iterate through both lists at the same time.
- In each iteration, print a string that says "[Student Name]'s score is [Score]".

Solution:
"""

# Example usage:
if __name__ == "__main__":
    students = ["Alice", "Bob", "Charlie", "David"]
    scores = [85, 92, 78, 88]
    
    print("--- Student Scores ---")
    
    # zip() pairs the elements from the two lists together:
    # ('Alice', 85), ('Bob', 92), etc.
    for name, score in zip(students, scores):
        print(f"{name}'s score is {score}")
        
    print("\n--- Note on zip() with lists of different lengths ---")
    # zip stops when the shortest iterable is exhausted.
    short_list = [1, 2, 3]
    long_list = ['a', 'b', 'c', 'd', 'e']
    zipped_pairs = list(zip(short_list, long_list))
    
    print(f"Zipping a short list {short_list} and a long list {long_list}")
    print(f"Result: {zipped_pairs}")


"""
Expected Output:

--- Student Scores ---
Alice's score is 85
Bob's score is 92
Charlie's score is 78
David's score is 88

--- Note on zip() with lists of different lengths ---
Zipping a short list [1, 2, 3] and a long list ['a', 'b', 'c', 'd', 'e']
Result: [(1, 'a'), (2, 'b'), (3, 'c')]
""" 