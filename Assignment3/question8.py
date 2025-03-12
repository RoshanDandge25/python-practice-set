def calculate_price():
    unit_price = 5  # Price per unit
    quantity = int(input("Enter the quantity: "))  # Get user input


    if quantity > 50:
        discount = 0.15
    elif quantity > 30:
        discount = 0.10
    else:
        discount = 0.00  #

    total_price = quantity * unit_price
    discount_amount = total_price * discount
    final_price = total_price - discount_amount


    print(f"Total price before discount: Rs {total_price:.2f}")
    print(f"Discount applied: Rs {discount_amount:.2f}")
    print(f"Final price after discount: Rs {final_price:.2f}")


calculate_price()
