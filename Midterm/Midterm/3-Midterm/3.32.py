# Function to calculate exchange money from Dollar to Riel
def exchange_dollar_to_riel(dollar, exchange_rate):
    return dollar * exchange_rate

# Prompt the user for input
while True:
    dollar = float(input("Please Enter Dollar: "))
    exchange_rate = float(input("Please Enter Exchange Rate: "))
    exchange_money = exchange_dollar_to_riel(dollar, exchange_rate)
    print(f"Exchange Money Dollar to Riel is: {exchange_money}")

    # Ask if the user wants to continue
    continue_option = input("Would you like to continue[y/n]?: ")
    if continue_option.lower() != 'y':
        print("Good bye!")
        break
