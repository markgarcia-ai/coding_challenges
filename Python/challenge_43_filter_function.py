"""
Challenge 43: Filter Function

Problem Statement:
Write a function that filters a list of strings to keep only those that are palindromes. A palindrome is a word that reads the same forwards and backwards.

Requirements:
- The function should be named `filter_palindromes`.
- It should accept one argument: a list of strings.
- Use the `filter` function to apply a filtering condition.
- The filtering logic should be case-insensitive.
- The function should return a new list containing only the palindromic strings.

Solution:
"""

def is_palindrome(s):
    """Checks if a string is a palindrome (case-insensitive)."""
    s_lower = s.lower()
    return s_lower == s_lower[::-1]

def filter_palindromes(words):
    """
    Filters a list of strings to keep only palindromes using the filter function.
    """
    return list(filter(is_palindrome, words))

# Example usage:
if __name__ == "__main__":
    word_list = ["madam", "hello", "level", "world", "Racecar", "python", "kayak"]
    palindromes = filter_palindromes(word_list)
    
    print(f"Original list: {word_list}")
    print(f"Palindromes: {palindromes}")

"""
Expected Output:

Original list: ['madam', 'hello', 'level', 'world', 'Racecar', 'python', 'kayak']
Palindromes: ['madam', 'level', 'Racecar', 'kayak']
""" 