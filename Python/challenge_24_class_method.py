"""
Challenge 24: Class Methods

Problem Statement:
Create a `User` class that uses a class method as a factory to create user instances from a dictionary. Class methods are bound to the class and not the instance, and they are often used for factory patterns.

Requirements:
- Create a class named `User`.
- The `__init__` method should accept `username` and `email`.
- Create a class method named `from_dict` decorated with `@classmethod`.
- `from_dict` should accept the class itself (`cls`) as the first argument and a dictionary `user_data` as the second.
- The `user_data` dictionary will have keys 'username' and 'email'.
- The class method should return a new instance of the `User` class.

Solution:
"""

class User:
    def __init__(self, username, email):
        """Initializes a User instance."""
        self.username = username
        self.email = email

    @classmethod
    def from_dict(cls, user_data):
        """Creates a User instance from a dictionary."""
        return cls(user_data['username'], user_data['email'])

    def display(self):
        """Displays user information."""
        return f"User: {self.username}, Email: {self.email}"

# Example usage:
if __name__ == "__main__":
    user_data_1 = {'username': 'jdoe', 'email': 'john.doe@example.com'}
    user_data_2 = {'username': 'asmith', 'email': 'anna.smith@example.com'}
    
    # Create user instances using the class method factory
    user1 = User.from_dict(user_data_1)
    user2 = User.from_dict(user_data_2)
    
    print(user1.display())
    print(user2.display())

"""
Expected Output:

User: jdoe, Email: john.doe@example.com
User: asmith, Email: anna.smith@example.com
""" 