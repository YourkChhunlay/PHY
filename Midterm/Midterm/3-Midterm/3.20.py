# Generate the series
for i in range(9, 0, -1):
    series = ''.join(str(j) for j in range(1, i + 1))
    print(series)
