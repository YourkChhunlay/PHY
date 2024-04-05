# Function to calculate insurance wage
def calculate_insurance_wage(monthly_wage):
    assumed_wages = {
        200000: 200000,
        250000: 225000,
        300000: 275000,
        350000: 325000,
        400000: 375000,
        450000: 425000,
        500000: 475000,
        550000: 525000,
        600000: 575000,
        650000: 625000,
        700000: 675000,
        750000: 725000,
        800000: 775000,
        850000: 825000,
        900000: 875000,
        950000: 925000,
        1000000: 1000000
    }

    for assumed, actual in assumed_wages.items():
        if monthly_wage <= assumed:
            return actual

# Prompt the user for input
while True:
    monthly_wage = float(input("Monthly Wage (Riel): "))
    assumed_wage = calculate_insurance_wage(monthly_wage)
    print(f"Assumed Wage: {assumed_wage}")

    # Ask if the user wants to continue
    continue_option = input("Would you like to continue[y/n]?: ")
    if continue_option.lower() != 'y':
        print("Good bye!")
        break
