# Function to calculate the exchange money from Riel to Dollar
def riel_to_dollar_exchange(riel, exchange_rate):
    dollar = riel / exchange_rate
    return dollar

# Prompt the user for input
riel = float(input("Enter the amount in Riel: "))
exchange_rate = float(input("Enter the exchange rate: "))

# Calculate and display the result
dollar_result = riel_to_dollar_exchange(riel, exchange_rate)
print(f"Exchange Money Riel to Dollar: {dollar_result}")
