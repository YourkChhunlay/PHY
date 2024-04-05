# Function to calculate exchange money from Riel to Dollar
def exchange_riel_to_dollar(riel, exchange_rate):
    return riel / exchange_rate

# Prompt the user for input
while True:
    riel = float(input("Please Enter Riel: "))
    exchange_rate = float(input("Please Enter Exchange Rate: "))
    exchange_money = exchange_riel_to_dollar(riel, exchange_rate)
    print(f"Exchange Money Riel to Dollar is: {exchange_money}")

    # Ask if the user wants to continue
    continue_option = input("Would you like to continue[y/n]?: ")
    if continue_option.lower() != 'y':
        print("Good bye!")
        break
