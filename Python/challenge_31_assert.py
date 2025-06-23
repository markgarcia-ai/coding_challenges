"""
Challenge 31: `assert` statement

Problem Statement:
Write a function that calculates the discount for a shopping cart. Use an `assert` statement to ensure that the discount percentage passed to the function is within a valid range (e.g., between 0 and 100).

Requirements:
- Create a function `apply_discount(price, discount_percentage)`.
- Inside the function, use `assert` to check if `0 <= discount_percentage <= 100`.
- If the assertion passes, the function should calculate and return the price after the discount.
- If the assertion fails, it should raise an `AssertionError`.
- Demonstrate a successful call and a call that triggers the assertion.

Solution:
"""

def apply_discount(price, discount_percentage):
    """
    Applies a discount to a price.
    Asserts that the discount percentage is valid.
    """
    # The assert statement checks a condition. If it's False, it raises an AssertionError.
    assert 0 <= discount_percentage <= 100, "Discount percentage must be between 0 and 100."
    
    discount_amount = price * (discount_percentage / 100)
    return price - discount_amount

# Example usage:
if __name__ == "__main__":
    # --- Valid case ---
    price = 200
    discount = 15
    final_price = apply_discount(price, discount)
    print(f"Original Price: ${price}, Discount: {discount}%, Final Price: ${final_price}")
    
    # --- Invalid case ---
    print("\n--- Now, attempting to use an invalid discount ---")
    try:
        invalid_discount = 110
        apply_discount(price, invalid_discount)
    except AssertionError as e:
        print(f"Caught expected error: {e}")

"""
Expected Output:

Original Price: $200, Discount: 15%, Final Price: $170.0

--- Now, attempting to use an invalid discount ---
Caught expected error: Discount percentage must be between 0 and 100.
""" 