# Function to calculate the exchange money from Dollar to Riel
def dollar_to_riel_exchange(dollar, exchange_rate):
    riel = dollar * exchange_rate
    return riel

# Prompt the user for input
dollar = float(input("Enter the amount in Dollar: "))
exchange_rate = float(input("Enter the exchange rate: "))

# Calculate and display the result
riel_result = dollar_to_riel_exchange(dollar, exchange_rate)
print(f"Exchange Money Dollar to Riel: {riel_result}")
