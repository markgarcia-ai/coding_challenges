"""
Challenge 8: Objects

Problem Statement:
Define a `Book` class to create objects that represent books. Each book object should have its own data (title and author) and behavior (a method to display its information).

Requirements:
- Create a class named `Book`.
- The class constructor (`__init__`) should initialize two attributes: `title` and `author`.
- The class should have a method `get_info()` that returns a string in the format: "'[title]' by [author]".
- Create two different `Book` objects (instances of the `Book` class) with different titles and authors.
- Call the `get_info()` method on each object to show that each object maintains its own separate data.

Solution:
"""

class Book:
    """Represents a book with a title and an author."""
    def __init__(self, title, author):
        # These are the attributes of a Book object.
        self.title = title
        self.author = author

    def get_info(self):
        # This is a method (behavior) of a Book object.
        return f"'{self.title}' by {self.author}"

# Example usage:
if __name__ == "__main__":
    # book1 is an object (an instance of the Book class)
    book1 = Book("1984", "George Orwell")
    
    # book2 is another, separate object
    book2 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
    
    # Each object holds its own data
    print(f"Book 1 info: {book1.get_info()}")
    print(f"Book 2 info: {book2.get_info()}")

"""
Expected Output:

Book 1 info: '1984' by George Orwell
Book 2 info: 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams
""" 