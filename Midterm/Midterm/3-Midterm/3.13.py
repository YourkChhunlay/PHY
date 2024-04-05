# Using while loop
print("Number\tSquare")
num = 1
while num <= 50:
    square = num ** 2
    print(f"{num}\t{square}")
    num += 1

# Using do-while loop (Python doesn't have a direct do-while loop, so we simulate it)
num = 1
print("Number\tSquare")
while True:
    square = num ** 2
    print(f"{num}\t{square}")
    num += 1
    if num > 50:
        break

# Using for loops
print("Number\tSquare")
for num in range(1, 101):
    square = num ** 2
    print(f"{num}\t{square}")
