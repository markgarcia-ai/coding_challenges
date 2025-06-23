"""
Challenge 65: Combined Challenge - Log Analyzer

Problem Statement:
Read the `sample.log` file, parse each line to extract the log level (INFO, WARNING, ERROR, DEBUG),
count the occurrences of each level, and print a summary report.

Recommended Concepts:
- `pathlib` for file path management.
- `with open()` for safely reading the file.
- `collections.Counter` for efficient counting.
- String `split()` method for parsing.
- `for` loops for iteration.
- A main function to organize the code.

Solution:
"""
from pathlib import Path
from collections import Counter

def analyze_log_file(file_path):
    """
    Reads a log file, counts log levels, and returns a Counter object.
    
    Args:
        file_path (Path): The path to the log file.
        
    Returns:
        Counter: A Counter object with counts for each log level.
    """
    log_levels = []
    
    # Ensure the file exists before trying to read it
    if not file_path.exists():
        print(f"Error: Log file not found at '{file_path}'")
        return None
        
    # Use 'with open' to ensure the file is properly closed
    with open(file_path, 'r') as f:
        for line in f:
            # Clean up the line and split it into parts
            parts = line.strip().split(' - ')
            # The log level is expected to be the second part
            if len(parts) > 1:
                log_levels.append(parts[1])
                
    return Counter(log_levels)

# Example usage:
if __name__ == "__main__":
    # Define the path to the log file
    log_file = Path("sample.log")
    
    # Analyze the file
    level_counts = analyze_log_file(log_file)
    
    # Print the report
    if level_counts:
        print("--- Log Analysis Report ---")
        for level, count in level_counts.items():
            print(f"- {level}: {count} occurrences")
        print("-------------------------")

"""
Expected Output:

--- Log Analysis Report ---
- INFO: 6 occurrences
- DEBUG: 3 occurrences
- WARNING: 2 occurrences
- ERROR: 3 occurrences
-------------------------
""" 