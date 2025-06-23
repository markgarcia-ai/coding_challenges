"""
Challenge 59: `collections.Counter`

Problem Statement:
Use `collections.Counter` to count the occurrences of items in a list. Then, use its built-in method to find the most common items.

Requirements:
- Import `Counter` from the `collections` module.
- Create a list of items with several duplicates (e.g., representing votes or items sold).
- Create a `Counter` object from the list.
- Print the `Counter` object to see the counts of each item.
- Use the `.most_common()` method to get the top 2 most common items and their counts.

Solution:
"""
from collections import Counter

# Example usage:
if __name__ == "__main__":
    # A list of votes for different fruits
    votes = [
        "apple", "banana", "apple", "orange", "banana",
        "apple", "grape", "banana", "orange", "apple"
    ]
    
    print(f"Original list of votes: {votes}\n")
    
    # Create a Counter object to count the items
    vote_counts = Counter(votes)
    
    print("--- Vote Counts ---")
    print(vote_counts)
    print(f"The count for 'apple' is: {vote_counts['apple']}")
    
    # Find the 2 most common items
    top_2 = vote_counts.most_common(2)
    
    print("\n--- Top 2 Most Common Fruits ---")
    print(top_2)
    print(f"The most common fruit is '{top_2[0][0]}' with {top_2[0][1]} votes.")

"""
Expected Output:

Original list of votes: ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'grape', 'banana', 'orange', 'apple']

--- Vote Counts ---
Counter({'apple': 4, 'banana': 3, 'orange': 2, 'grape': 1})
The count for 'apple' is: 4

--- Top 2 Most Common Fruits ---
[('apple', 4), ('banana', 3)]
The most common fruit is 'apple' with 4 votes.
""" 