user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

#returns keys
for item in user:
    print(item)

#returns tuples
for item in user.items():
    print(item)

#returns tuple keys and values
for key, value in user.items():
    print(key, value)

#returns values
for item in user.values():
    print(item)

#returns keys
for item in user.keys():
    print(item)