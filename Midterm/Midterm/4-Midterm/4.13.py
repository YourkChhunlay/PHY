# Function to swap two data items
def swap_data(n, m):
    print(f"Before swap: N = {n}, M = {m}")
    n, m = m, n  # swapping
    print(f"After swap: N = {n}, M = {m}")

# Prompt the user for input
n = float(input("Enter the value for N: "))
m = float(input("Enter the value for M: "))

# Perform and display the swap
swap_data(n, m)
