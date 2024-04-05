# a) sum=1+2+3+….+n = ?
n = int(input("Enter the value of n: "))
sum_a = sum(range(1, n + 1))
print(f"a) sum=1+2+3+….+n = {sum_a}")

# b) sum=1+3+5+….+n = ?
sum_b = sum(range(1, n + 1, 2))
print(f"b) sum=1+3+5+….+n = {sum_b}")

# c) sum=1+2+4+….+n = ?
sum_c = sum(2 ** i for i in range(n))
print(f"c) sum=1+2+4+….+n = {sum_c}")

# d) sum=12+22+32+….+n2 = ?
sum_d = sum(i**2 for i in range(1, n + 1, 10))
print(f"d) sum=12+22+32+….+n2 = {sum_d}")

# e) sum=12+32+52+….+n2
sum_e = sum(i**2 for i in range(1, n + 1, 20))
print(f"e) sum=12+32+52+….+n2 = {sum_e}")

# f) sum=12+22+42+….+n2
sum_f = sum(i**2 for i in range(1, n + 1, 10))
print(f"f) sum=12+22+42+….+n2 = {sum_f}")
