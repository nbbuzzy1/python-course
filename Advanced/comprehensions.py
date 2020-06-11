#list, set, dictionary

my_list = [char for char in 'hello']
my_list2 = [num * 2 for num in range(100)]
my_list3 = [num ** 2 for num in range(100) if num % 2 == 0]

# instead of:

my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)
print(my_list2)

# set

my_list = {char for char in 'hello'}
my_list2 = {num * 2 for num in range(100)}
my_list3 = {num ** 2 for num in range(100) if num % 2 == 0}

# dictionary
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key: value**2 for key, value in simple_dict.items() if value > 1}

print(simple_dict.items())
print(my_dict)

my_dict2 = {num: num*2 for num in [1, 2, 3]}
print(my_dict2)
