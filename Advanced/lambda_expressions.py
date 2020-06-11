# lambda param: action(param)

from functools import reduce

# multiply by 2

my_list = [1, 2, 3]

print(list(map(lambda item: item*2, my_list)))

print(reduce(lambda acc, item: item+acc, my_list))
