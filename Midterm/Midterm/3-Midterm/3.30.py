# Function to calculate selling price with discount
def calculate_selling_price(weight):
    base_price = 1200  # Base price per kg
    discount_threshold_1 = 100  # Discount applies for 100kg to 500kg
    discount_threshold_2 = 500  # Discount applies for over 500kg
    discount_rate_1 = 15  # 15% discount for 100kg to 500kg
    discount_rate_2 = 25  # 25% discount for over 500kg

    if 0 < weight <= discount_threshold_1:
        return base_price * weight
    elif discount_threshold_1 < weight <= discount_threshold_2:
        discount_amount = (base_price * weight * discount_rate_1) / 100
        return base_price * weight - discount_amount
    elif weight > discount_threshold_2:
        discount_amount = (base_price * weight * discount_rate_2) / 100
        return base_price * weight - discount_amount

# Prompt the user for input
while True:
    weight = int(input("The weight of rice: "))
    selling_price = calculate_selling_price(weight)
    print(f"Selling Price: {selling_price}")

    # Ask if the user wants to continue
    continue_option = input("Would you like to continue[y/n]?: ")
    if continue_option.lower() != 'y':
        print("Good bye!")
        break
