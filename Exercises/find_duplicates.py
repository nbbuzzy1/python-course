# Check for duplicates in a list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# my answer
duplicates = []
for i, item in enumerate(some_list):
    if i != some_list.index(item):
        duplicates.append(item)
print(duplicates)

# class answer
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
