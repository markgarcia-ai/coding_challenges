"""
Challenge 2: Dictionaries

Problem Statement:
Write a function that counts the frequency of each word in a given text string.

Requirements:
- The function should be named `count_word_frequency`.
- It should accept one argument: a string of text.
- The function should return a dictionary where keys are the words and values are their frequencies.
- The counting should be case-insensitive (e.g., "Hello" and "hello" are the same word).
- Punctuation should be ignored.

Solution:
"""
import re

def count_word_frequency(text):
    """
    Counts the frequency of each word in a text.
    """
    words = re.findall(r'\b\w+\b', text.lower())
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Example usage:
if __name__ == "__main__":
    text_block = "Hello world! This is a test. Hello everyone, this is a simple test."
    word_counts = count_word_frequency(text_block)
    print(f"Text: \"{text_block}\"")
    print("Word Frequencies:")
    # Print sorted for consistent output
    for word, count in sorted(word_counts.items()):
        print(f"  '{word}': {count}")

"""
Expected Output:

Text: "Hello world! This is a test. Hello everyone, this is a simple test."
Word Frequencies:
  'a': 2
  'everyone': 1
  'hello': 2
  'is': 2
  'simple': 1
  'test': 2
  'this': 2
  'world': 1
""" 