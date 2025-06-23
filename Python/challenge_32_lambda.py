"""
Challenge 32: Lambda Functions

Problem Statement:
You have a list of tuples, where each tuple contains a student's name (string) and their grade (integer). Write a function to sort the list of students based on their grades in descending order.

Requirements:
- The function should be named `sort_students_by_grade`.
- It should accept one argument: a list of student tuples `(name, grade)`.
- Use the built-in `sorted()` function.
- For the `key` argument of the `sorted()` function, use a `lambda` function to specify that the sorting should be based on the grade (the second item in the tuple).
- The list should be sorted in descending (highest to lowest) order.

Solution:
"""

def sort_students_by_grade(students):
    """
    Sorts a list of student tuples by grade in descending order using a lambda function.
    """
    return sorted(students, key=lambda student: student[1], reverse=True)

# Example usage:
if __name__ == "__main__":
    student_grades = [
        ("Alice", 88),
        ("Bob", 95),
        ("Charlie", 78),
        ("Diana", 92),
        ("Eve", 85)
    ]
    
    sorted_students = sort_students_by_grade(student_grades)
    
    print(f"Original list: {student_grades}")
    print(f"Sorted list by grade (descending): {sorted_students}")

"""
Expected Output:

Original list: [('Alice', 88), ('Bob', 95), ('Charlie', 78), ('Diana', 92), ('Eve', 85)]
Sorted list by grade (descending): [('Bob', 95), ('Diana', 92), ('Alice', 88), ('Eve', 85), ('Charlie', 78)]
""" 