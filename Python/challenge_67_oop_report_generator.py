"""
Challenge 67: Combined Challenge - OOP Report Generator

Problem Statement:
Given a list of raw sales data (dictionaries), model the data using classes
and generate a sales report showing total revenue per product.

Recommended Concepts:
- Classes and Objects to model `Product` and `Sale`.
- `datetime` module for parsing date strings into objects.
- Dictionaries for aggregating revenue data.
- String formatting for a clean report.

Solution:
"""
from datetime import datetime

# --- Data Models (Classes) ---
class Product:
    """Represents a product with an ID and a name."""
    def __init__(self, product_id: str, name: str):
        self.product_id = product_id
        self.name = name

class Sale:
    """Represents a single sale event."""
    def __init__(self, product: Product, quantity: int, price_per_unit: float, sale_date: str):
        self.product = product
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.sale_date = datetime.strptime(sale_date, "%Y-%m-%d")
        self.total_price = quantity * price_per_unit

# --- Report Generation Logic ---
def generate_product_revenue_report(sales_list: list):
    """
    Processes a list of Sale objects and prints a revenue report.
    """
    revenue_by_product = {} # Using a dict to aggregate revenue

    for sale in sales_list:
        product_name = sale.product.name
        # Add the sale's total price to the correct product entry
        if product_name not in revenue_by_product:
            revenue_by_product[product_name] = 0
        revenue_by_product[product_name] += sale.total_price
        
    # --- Print the formatted report ---
    print("--- Product Revenue Report ---")
    for product, total_revenue in revenue_by_product.items():
        print(f"- {product:<15}: ${total_revenue:,.2f}")
    print("----------------------------")

# Example usage:
if __name__ == "__main__":
    # --- Raw Data and Object Creation ---
    # In a real app, this data might come from a DB or CSV file.
    p1 = Product("P001", "Laptop")
    p2 = Product("P002", "Mouse")
    p3 = Product("P003", "Keyboard")
    
    sales_data = [
        Sale(p1, 5, 1200.00, "2023-10-01"),
        Sale(p2, 10, 25.50, "2023-10-01"),
        Sale(p3, 8, 75.00, "2023-10-02"),
        Sale(p1, 2, 1150.00, "2023-10-03"), # Different price
        Sale(p2, 15, 25.00, "2023-10-04"),
    ]
    
    # --- Generate the Report ---
    generate_product_revenue_report(sales_data)

"""
Expected Output:

--- Product Revenue Report ---
- Laptop         : $8,300.00
- Mouse          : $630.00
- Keyboard       : $600.00
----------------------------
""" 