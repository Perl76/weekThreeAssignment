#question one code
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price

#question two code
def calculate_and_display_final_price():
    price = float(input("Enter the original price of the item: "))
    discount_percent = int(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(price, discount_percent)
    
    if final_price != price:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"The original price remains: ${price:.2f} as the discount is less than 20%.")

# Call the function to prompt and display the result
calculate_and_display_final_price()
