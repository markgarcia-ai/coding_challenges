"""
Challenge 14: Aggregation

Problem Statement:
Model a `Department` that has a list of `Professor` objects. This is an aggregation relationship because a `Professor` can exist independently of a `Department`. The `Department` does not create or destroy `Professor` objects.

Requirements:
- Create a `Professor` class with a `name` attribute.
- Create a `Department` class.
- The `Department`'s `__init__` method should take a `name` (e.g., "Computer Science") and initialize an empty list to hold professors.
- Create a method `add_professor(self, professor)` in the `Department` class that adds a `Professor` object to its list.
- Create a method `list_professors(self)` that prints the names of all professors in that department.

Solution:
"""

class Professor:
    """A simple class to represent a professor."""
    def __init__(self, name):
        self.name = name

class Department:
    """A class that aggregates Professor objects."""
    def __init__(self, name):
        self.name = name
        self.professors = []

    def add_professor(self, professor):
        """Adds a professor to the department."""
        self.professors.append(professor)

    def list_professors(self):
        """Lists the professors in the department."""
        print(f"Department: {self.name}")
        for prof in self.professors:
            print(f" - {prof.name}")

# Example usage:
if __name__ == "__main__":
    # Create professor objects. They exist independently.
    prof1 = Professor("Dr. Smith")
    prof2 = Professor("Dr. Jones")
    
    # Create a department
    cs_department = Department("Computer Science")
    
    # Add professors to the department
    cs_department.add_professor(prof1)
    cs_department.add_professor(prof2)
    
    cs_department.list_professors()

"""
Expected Output:

Department: Computer Science
 - Dr. Smith
 - Dr. Jones
""" 