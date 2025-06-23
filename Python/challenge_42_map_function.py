"""
Challenge 42: Map Function

Problem Statement:
Write a function that converts a list of temperatures from Celsius to Fahrenheit.

Requirements:
- The function should be named `celsius_to_fahrenheit_list`.
- It should accept one argument: a list of temperatures in Celsius.
- Use the `map` function to apply the conversion formula to each temperature.
- The conversion formula is: Fahrenheit = (Celsius * 9/5) + 32.
- The function should return a new list of temperatures in Fahrenheit.

Solution:
"""

def celsius_to_fahrenheit(celsius):
    """Converts a single temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def celsius_to_fahrenheit_list(celsius_temps):
    """
    Converts a list of Celsius temperatures to Fahrenheit using the map function.
    """
    return list(map(celsius_to_fahrenheit, celsius_temps))

# Example usage:
if __name__ == "__main__":
    celsius_temperatures = [0, 10, 25, 30, 100]
    fahrenheit_temperatures = celsius_to_fahrenheit_list(celsius_temperatures)
    
    print(f"Celsius temperatures: {celsius_temperatures}")
    print(f"Fahrenheit temperatures: {fahrenheit_temperatures}")

"""
Expected Output:

Celsius temperatures: [0, 10, 25, 30, 100]
Fahrenheit temperatures: [32.0, 50.0, 77.0, 86.0, 212.0]
""" 