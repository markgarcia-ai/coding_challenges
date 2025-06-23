"""
Challenge 11: Instance

Problem Statement:
Create a `Student` class and then create two separate instances of it. Demonstrate that each instance has its own set of data (attributes) and that changing one instance does not affect the other.

Requirements:
- Create a class named `Student`.
- The `__init__` method should take a `student_id` and initialize an empty list called `grades`.
- Create a method `add_grade(self, grade)` that adds a grade to the instance's `grades` list.
- Create a method `show_grades(self)` that prints the student's ID and their list of grades.
- In the main block, create two `Student` instances. Add different grades to each and display their grades to show they are independent.

Solution:
"""

class Student:
    """Represents a single student, acting as a blueprint."""
    def __init__(self, student_id):
        # Each instance will get its own student_id and grades list
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def show_grades(self):
        print(f"Student ID: {self.student_id}, Grades: {self.grades}")

# Example usage:
if __name__ == "__main__":
    # student1 is an instance of the Student class.
    student1 = Student("S101")
    
    # student2 is another, completely separate instance.
    student2 = Student("S102")
    
    # Add grades to the first instance
    student1.add_grade(95)
    student1.add_grade(88)
    
    # Add grades to the second instance
    student2.add_grade(76)
    student2.add_grade(82)
    
    # Displaying the grades shows that each instance has its own data
    print("Displaying grades for each instance:")
    student1.show_grades()
    student2.show_grades()

"""
Expected Output:

Displaying grades for each instance:
Student ID: S101, Grades: [95, 88]
Student ID: S102, Grades: [76, 82]
""" 