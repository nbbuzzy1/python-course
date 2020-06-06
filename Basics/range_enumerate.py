# range
print(range(0, 100))

for num in range(10, 0, -2):
    print(num)

print(list(range(10)))

# enumerate
for char in enumerate('Hello'):
    print(char)

for i, char in enumerate('Hello'):
    print(i, char)

for i, char in enumerate((1, 2, 3)):
    print(i, char)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(i)
