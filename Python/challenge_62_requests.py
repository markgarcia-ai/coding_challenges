"""
Challenge 62: `requests` for HTTP GET Requests

Problem Statement:
Use the `requests` library to make a GET request to a public API and process the JSON response. We will use the JSONPlaceholder API, which is a fake online REST API for testing.

Requirements:
- You must first install the `requests` library: `pip install requests`
- Import the `requests` module.
- Make a GET request to `https://jsonplaceholder.typicode.com/todos/1`.
- Check if the request was successful by checking the status code.
- If successful, parse the JSON response and print the title and completion status of the to-do item.
- If not successful, print an error message with the status code.

Solution:
"""
import requests

def fetch_todo_item(item_id):
    """Fetches a to-do item from the JSONPlaceholder API."""
    
    url = f"https://jsonplaceholder.typicode.com/todos/{item_id}"
    print(f"Fetching data from: {url}")

    try:
        response = requests.get(url)
        
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()

        # If the request was successful, process the JSON data
        todo_item = response.json()
        
        print("\n--- Request Successful ---")
        print(f"User ID: {todo_item['userId']}")
        print(f"Title: {todo_item['title']}")
        print(f"Completed: {todo_item['completed']}")

    except requests.exceptions.RequestException as e:
        print(f"\n--- Request Failed ---")
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    fetch_todo_item(1)

"""
Expected Output:

Fetching data from: https://jsonplaceholder.typicode.com/todos/1

--- Request Successful ---
User ID: 1
Title: delectus aut autem
Completed: False
""" 