#List unpacking

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a, b, c, d)
print(*other)