"""
Challenge 48: argparse

Problem Statement:
Create a simple command-line tool that greets a user. The tool should accept the user's name as a required argument and an optional argument to make the greeting uppercase.

Requirements:
- Use the `argparse` module.
- The script should accept one positional argument: `name`.
- It should accept an optional flag: `--uppercase` or `-u`.
- If the `--uppercase` flag is present, the entire output should be in uppercase.
- When run, the script should print a greeting like "Hello, [name]!".

Solution:
"""
import argparse

def greet_user(name, is_uppercase):
    """Constructs and prints the greeting."""
    message = f"Hello, {name}!"
    if is_uppercase:
        message = message.upper()
    print(message)

def main():
    """Main function to parse arguments and call the greeting logic."""
    # 1. Create the parser
    parser = argparse.ArgumentParser(description="A simple tool to greet a user.")
    
    # 2. Add arguments
    # Positional argument
    parser.add_argument("name", help="The name of the person to greet.")
    # Optional flag argument
    parser.add_argument(
        "-u", "--uppercase", 
        action="store_true", # Makes it a flag (stores True if present)
        help="Display the greeting in uppercase."
    )
    
    # 3. Parse the arguments
    args = parser.parse_args()
    
    # 4. Use the arguments
    greet_user(args.name, args.uppercase)

if __name__ == "__main__":
    main()

"""
How to Run from Command Line:

1. Save the code as `greet_tool.py`.
2. Open your terminal or command prompt.
3. Run the following commands to see the output:

   # Basic usage
   python greet_tool.py Alice
   
   # With the uppercase flag
   python greet_tool.py Bob --uppercase
   
   # Using the short flag
   python greet_tool.py Charlie -u
   
   # With the --help flag (auto-generated)
   python greet_tool.py --help

Expected Output:

# For `python greet_tool.py Alice`
Hello, Alice!

# For `python greet_tool.py Bob --uppercase`
HELLO, BOB!

# For `python greet_tool.py Charlie -u`
HELLO, CHARLIE!
""" 