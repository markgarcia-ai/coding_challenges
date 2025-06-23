"""
Challenge 19: super()

Problem Statement:
Create a `Manager` class that inherits from an `Employee` class. The `Manager` should extend the `Employee`'s `__init__` method to add a `department` attribute, using `super()` to call the parent constructor.

Requirements:
- Create a base class `Employee` with an `__init__` method that takes `name` and `salary`. It should store these as attributes.
- The `Employee` class should also have a `display()` method that prints the name and salary.
- Create a `Manager` class that inherits from `Employee`.
- The `Manager`'s `__init__` method should take `name`, `salary`, and `department`.
- Inside the `Manager`'s `__init__`, use `super().__init__(name, salary)` to call the `Employee` constructor.
- The `Manager` should also override the `display()` method to print the department in addition to the name and salary, calling `super().display()` to avoid duplicating code.

Solution:
"""

class Employee:
    """A base class for an employee."""
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: ${self.salary:,}")

class Manager(Employee):
    """A subclass for a manager."""
    def __init__(self, name, salary, department):
        # Use super() to call the __init__ of the parent class (Employee)
        super().__init__(name, salary)
        # Add the new attribute specific to Manager
        self.department = department

    def display(self):
        # Call the parent's display method to print name and salary
        super().display()
        # Print the information specific to the Manager
        print(f"Department: {self.department}")

# Example usage:
if __name__ == "__main__":
    emp = Employee("John Doe", 60000)
    mgr = Manager("Jane Smith", 90000, "Engineering")
    
    print("Employee Details:")
    emp.display()
    
    print("\nManager Details:")
    mgr.display()

"""
Expected Output:

Employee Details:
Name: John Doe, Salary: $60,000

Manager Details:
Name: Jane Smith, Salary: $90,000
Department: Engineering
""" 