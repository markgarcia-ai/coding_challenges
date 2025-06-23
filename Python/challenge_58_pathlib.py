"""
Challenge 58: `pathlib` for File System Interaction

Problem Statement:
Use the `pathlib` module to perform basic file system operations: create a directory, create and write to a file within it, and then list the contents of that directory.

Requirements:
- Import the `Path` object from the `pathlib` module.
- **Task 1**: Create a `Path` object representing a new directory named `test_data`. Create this directory using the `.mkdir()` method.
- **Task 2**: Create a `Path` object for a new file `notes.txt` inside the `test_data` directory.
- **Task 3**: Write some text to this file using the `.write_text()` method.
- **Task 4**: List all the files and directories inside `test_data` using the `.iterdir()` method.
- **Bonus**: Clean up by deleting the file and then the directory.

Solution:
"""
from pathlib import Path

# Example usage:
if __name__ == "__main__":
    # The current working directory
    base_path = Path('.')
    
    # 1. Create a Path object for the new directory
    data_dir = base_path / 'test_data'
    
    # Create the directory, `exist_ok=True` prevents an error if it already exists
    data_dir.mkdir(exist_ok=True)
    print(f"Directory '{data_dir}' created or already exists.")
    
    # 2. Create a Path object for the new file
    file_path = data_dir / 'notes.txt'
    
    # 3. Write text to the file (UTF-8 by default)
    file_path.write_text("This is a sample note.\nPathlib makes file handling easy!")
    print(f"File '{file_path}' created and content written.")
    
    # 4. List the contents of the directory
    print(f"\n--- Contents of '{data_dir}' ---")
    for item in data_dir.iterdir():
        print(item)
    print("--------------------------")
    
    # Bonus: Clean up
    print("\n--- Cleaning up ---")
    file_path.unlink() # Delete the file
    print(f"Deleted file: '{file_path}'")
    data_dir.rmdir() # Delete the (now empty) directory
    print(f"Deleted directory: '{data_dir}'")
    print("-------------------")

"""
Expected Output:

Directory 'test_data' created or already exists.
File 'test_data/notes.txt' created and content written.

--- Contents of 'test_data' ---
test_data/notes.txt
--------------------------

--- Cleaning up ---
Deleted file: 'test_data/notes.txt'
Deleted directory: 'test_data'
-------------------
""" 