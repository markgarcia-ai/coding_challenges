"""
Challenge 3: Tuples

Problem Statement:
You are given a list of tuples, where each tuple contains a student's name and their score. Write a function to find the student with the highest score.

Requirements:
- The function should be named `find_top_student`.
- It should accept one argument: a list of tuples, where each tuple is `(name, score)`.
- The function should return the tuple of the student with the highest score.
- If the list is empty, it should return `None`.
- You must handle the data as tuples, demonstrating their use.

Solution:
"""

def find_top_student(students):
    """
    Finds the student with the highest score from a list of (name, score) tuples.
    """
    if not students:
        return None
        
    top_student = None
    max_score = -1
    
    for student_tuple in students:
        name, score = student_tuple  # Tuple unpacking
        if score > max_score:
            max_score = score
            top_student = student_tuple
            
    return top_student

# Example usage:
if __name__ == "__main__":
    student_scores = [
        ("Alice", 88),
        ("Bob", 95),
        ("Charlie", 78),
        ("Diana", 95),
        ("Eve", 85)
    ]
    
    top_performer = find_top_student(student_scores)
    print(f"Student data: {student_scores}")
    print(f"Top performing student: {top_performer}")

    empty_list = []
    top_performer = find_top_student(empty_list)
    print(f"Student data: {empty_list}")
    print(f"Top performing student: {top_performer}")


"""
Expected Output:

Student data: [('Alice', 88), ('Bob', 95), ('Charlie', 78), ('Diana', 95), ('Eve', 85)]
Top performing student: ('Bob', 95)
Student data: []
Top performing student: None
""" 