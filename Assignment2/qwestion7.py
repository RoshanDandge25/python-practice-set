def calculate_price(quantity):
    unit_price = 5  # Rs 5 per unit
    total_price = quantity * unit_price
    
    # Apply discounts
    if quantity > 50:
        discount = 0.15  # 15% discount
    elif quantity > 30:
        discount = 0.10  # 10% discount
    else:
        discount = 0  # No discount
    
    final_price = total_price - (total_price * discount)
    return final_price

# Take user input with error handling
try:
    quantity = int(input("Enter the quantity: "))
    if quantity < 0:
        print("Quantity cannot be negative. Please enter a valid number.")
    else:
        price = calculate_price(quantity)
        print(f"Total price after discount: Rs {price:.2f}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
