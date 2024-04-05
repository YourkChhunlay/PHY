# Generate the pyramid
for i in range(6):
    print(''.join(str(j) for j in range(i, -1, -1)))
