# Generate the series
for i in range(1, 10):
    series = ''.join(str(j) for j in range(i, 0, -1))
    print(series)
