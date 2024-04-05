# Function to calculate tax on salary
def calculate_tax(salary):
    if 0 < salary <= 500000:
        return 0
    elif 500001 <= salary <= 1250000:
        return (salary * 5 / 100) - 25000
    elif 1250001 <= salary <= 8500000:
        return (salary * 10 / 100) - 87500
    elif 8500001 <= salary <= 12500000:
        return (salary * 15 / 100) - 512500
    elif salary > 12500000:
        return (salary * 20 / 100) - 1137000

# Prompt the user for input
while True:
    salary = float(input("Monthly salary (Riels): "))
    tax = calculate_tax(salary)
    print(f"Tax on Salary: {tax}")

    # Ask if the user wants to continue
    continue_option = input("Would you like to continue[y/n]?: ")
    if continue_option.lower() != 'y':
        print("Good bye!")
        break
