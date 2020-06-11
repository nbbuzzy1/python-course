from functools import reduce

# map


def multiply_by2(item):
    return item*2


print(list(map(multiply_by2, [1, 2, 3])))

# filter


def check_odd(item):
    return item % 2 != 0


print(list(filter(check_odd, [1, 2, 3, 4])))

# zip

my_list = [1, 2, 3, 4]
your_list = [10, 20, 30, 4]

print(list(zip(my_list, your_list)))

# reduce (see functools above)


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_list, 10))
