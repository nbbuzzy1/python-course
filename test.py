#Dictionary

dictionary = {
    'a': 1,
    'b': 2
}

print(dictionary['b'])

# Keys

dictionary = {
    123: [1, 2, 3],
    True: 'hello'
}

# Methods

print(dictionary.get(123))
print(dictionary.get(123, 'hi'))
print(dictionary.get(123)) # these all return the same value

name = dict(name = 'nick', age = 12)
print(name)

print(123 in dictionary)
print('hello' in dictionary.values())
print(dictionary.items())