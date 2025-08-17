**Discount Calculator**
**Description**
This Python program calculates the final price of an item after applying a discount, based on the original price and the discount percentage. 
If the discount percentage is 20% or higher, the discount is applied; otherwise, the original price is maintained.

**Features**
Calculates discounted price for discounts of 20% or more
Returns original price for discounts below 20%
Handles user input for price and discount percentage
Displays formatted output with the final price

**How to Use**
Run the program in a Python environment
Enter the original price when prompted
Enter the discount percentage when prompted
The program will display either:
The discounted price (if discount is 20% or more)
The original price (if discount is less than 20%)

**Code Structure**
calculate_discount(price, discount_percent) function:
Takes price and discount percentage as arguments
Returns discounted price if discount is ≥20%
Returns original price otherwise

**Main program flow:**
Gets user input for price and discount percentage
Calls calculate_discount() function
Displays appropriate output message

**Example Usage**
text
Enter the original price: 1000
Enter the percentage discount: 25
Final price after 25.0% discount = Ksh. 750.00
text
Enter the original price: 500
Enter the percentage discount: 15
No discount applied. Original price = Ksh. 500.00
Requirements
Python 3.x

**Notes**
Prices are displayed with 2 decimal places
Currency is displayed in Kenyan Shillings (Ksh.) but can be modified as needed

**Rights**
The program is created by Samuel Oyuga. The code can be used freely by anybody who has access the repository link. 
