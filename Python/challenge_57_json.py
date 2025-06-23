"""
Challenge 57: `json` module

Problem Statement:
Use the `json` module to serialize a Python dictionary into a JSON string and then deserialize a JSON string back into a Python dictionary.

Requirements:
- Import the `json` module.
- **Task 1 (Serialization)**:
  - Create a Python dictionary representing a user profile.
  - Use `json.dumps()` to convert the dictionary into a JSON-formatted string.
  - Print the dictionary and the resulting JSON string.
- **Task 2 (Deserialization)**:
  - Create a JSON string representing a product.
  - Use `json.loads()` to parse the JSON string back into a Python dictionary.
  - Print the JSON string and the resulting Python dictionary.

Solution:
"""
import json

# Example usage:
if __name__ == "__main__":
    # --- Task 1: Serialize a Python dictionary to a JSON string ---
    print("--- 1. Python Dict -> JSON String (Serialization) ---")
    user_profile = {
        "name": "John Doe",
        "age": 30,
        "isStudent": False,
        "courses": ["History", "Math"]
    }
    
    # Use dumps() to write an object to a string. `indent=4` makes it readable.
    json_string = json.dumps(user_profile, indent=4)
    
    print("Original Python Dictionary:")
    print(user_profile)
    print("\nSerialized JSON String:")
    print(json_string)
    
    print("\n" + "="*40 + "\n")
    
    # --- Task 2: Deserialize a JSON string to a Python dictionary ---
    print("--- 2. JSON String -> Python Dict (Deserialization) ---")
    product_json = '{"productId": "P1234", "price": 49.99, "inStock": true}'
    
    # Use loads() to read an object from a string.
    product_dict = json.loads(product_json)
    
    print("Original JSON String:")
    print(product_json)
    print("\nDeserialized Python Dictionary:")
    print(product_dict)
    print(f"Product price is: ${product_dict['price']}")

"""
Expected Output:

--- 1. Python Dict -> JSON String (Serialization) ---
Original Python Dictionary:
{'name': 'John Doe', 'age': 30, 'isStudent': False, 'courses': ['History', 'Math']}

Serialized JSON String:
{
    "name": "John Doe",
    "age": 30,
    "isStudent": false,
    "courses": [
        "History",
        "Math"
    ]
}

========================================

--- 2. JSON String -> Python Dict (Deserialization) ---
Original JSON String:
{"productId": "P1234", "price": 49.99, "inStock": true}

Deserialized Python Dictionary:
{'productId': 'P1234', 'price': 49.99, 'inStock': True}
Product price is: $49.99
""" 