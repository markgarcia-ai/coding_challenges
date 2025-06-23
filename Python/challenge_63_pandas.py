"""
Challenge 63: `pandas` for Data Manipulation

Problem Statement:
Use the `pandas` library to create a `DataFrame` (a 2D labeled data structure), display it, and perform basic data selection and filtering.

Requirements:
- You must first install the `pandas` library: `pip install pandas`
- Import the `pandas` module.
- Create a Python dictionary to hold sample data about people (e.g., Name, Age, City).
- Convert this dictionary into a pandas `DataFrame`.
- Perform and print the results of the following operations:
  1.  Display the entire `DataFrame`.
  2.  Select and display just the 'Name' column.
  3.  Filter and display the rows for people older than 30.

Solution:
"""
import pandas as pd

# Example usage:
if __name__ == "__main__":
    # Create a dictionary of data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 32, 28, 45],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }
    
    # Create a pandas DataFrame from the dictionary
    df = pd.DataFrame(data)
    
    # 1. Display the entire DataFrame
    print("--- Full DataFrame ---")
    print(df)
    
    # 2. Select and display a single column (returns a pandas Series)
    print("\n--- 'Name' Column ---")
    print(df['Name'])
    
    # 3. Filter rows based on a condition
    print("\n--- People Older Than 30 ---")
    older_than_30 = df[df['Age'] > 30]
    print(older_than_30)

"""
Expected Output:

--- Full DataFrame ---
      Name  Age         City
0    Alice   25     New York
1      Bob   32  Los Angeles
2  Charlie   28      Chicago
3    David   45      Houston

--- 'Name' Column ---
0      Alice
1        Bob
2    Charlie
3      David
Name: Name, dtype: object

--- People Older Than 30 ---
    Name  Age         City
1    Bob   32  Los Angeles
3  David   45      Houston
""" 