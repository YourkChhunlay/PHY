# Function to generate monthly payment table for ABC MFI
def generate_monthly_payment(borrow, interest_rate, duration):
    monthly_payment_table = []

    # Calculate monthly payment for each month
    for month in range(1, duration + 1):
        if month == 1:
            balance = borrow
        else:
            balance -= borrow / duration

        interest_payment = (balance * interest_rate) / 100
        monthly_payment = (borrow / duration) + interest_payment

        monthly_payment_table.append([month, round(balance, 2), round(interest_payment, 2), round(borrow / duration, 2), round(monthly_payment, 2)])

    return monthly_payment_table

# Prompt the user for input
borrow = float(input("Enter Borrow Money: "))
interest_rate = float(input("Enter Interest Rate: "))
duration = int(input("Enter Duration (in months): "))

# Generate and display the monthly payment table
monthly_payment_table = generate_monthly_payment(borrow, interest_rate, duration)

# Display the Monthly Payment Table
print("\nMonthly Payment Table:")
print("Month\tBal\t\tIR\t\tDbal\t\tPay")
for row in monthly_payment_table:
    print(f"{row[0]}\t${row[1]}\t\t${row[2]}\t\t${row[3]}\t\t${row[4]}")
