# Use comprehensions to create a duplicate list

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

answer = list({item for item in some_list if some_list.count(item) > 1})
print(answer)
