# Logical operators

print(1 < 2 < 3 < 4) # prints true
print(0 <= 0)
print(0 != 1)

print(not('hi'))

is_magician = True
is_expert = False

if is_magician and is_expert:
    print('you are a master magician')
elif is_magician and not is_expert:
    print('at least you are getting there')
else:
    print('You need magic powers')