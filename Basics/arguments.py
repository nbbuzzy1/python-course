# *args **kwargs

def super_func(name, *args, i='hi', **kwargs):
    print(args)
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(super_func(1, 3, num1=5, num2=8))
