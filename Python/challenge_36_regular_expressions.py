"""
Challenge 36: Regular Expressions

Problem Statement:
Write a function that finds all valid email addresses in a given string of text.

Requirements:
- Use Python's built-in `re` module.
- The function should be named `find_emails`.
- It should accept one argument: a string `text`.
- The regular expression should be able to match common email formats (e.g., `user@domain.com`, `user.name@sub.domain.co.uk`).
- The function should return a list of all found email addresses.

Solution:
"""
import re

def find_emails(text):
    """
    Finds all valid email addresses in a string using regular expressions.
    """
    # A common regex for matching email addresses
    email_regex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    
    return re.findall(email_regex, text)

# Example usage:
if __name__ == "__main__":
    sample_text = """
    Please contact us at support@example.com for help.
    You can also reach out to john.doe@work-place.co.uk.
    This is not an email: user@.com. Invalid email: name@domain.
    Another valid one is jane_doe123@my-server.net.
    """
    
    emails = find_emails(sample_text)
    
    print("Found email addresses:")
    for email in emails:
        print(email)

"""
Expected Output:

Found email addresses:
support@example.com
john.doe@work-place.co.uk
jane_doe123@my-server.net
""" 