# Program to calculate discount based on price and percentage discount

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price

# Prompt user for input with error handling
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the percentage discount: "))
    
    # Display the results
    final_price = calculate_discount(price, discount_percent)  # call to calculate_discount function
    if discount_percent >= 20:
        print(f"Final price after {discount_percent}% discount = Ksh. {final_price:.2f}")
    else:
        print(f"No discount applied. Original price = Ksh. {final_price:.2f}")

except ValueError:
    print("Error: Please enter valid numeric values for both price and discount percentage.")