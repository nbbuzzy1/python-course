# They add the prior two numbers

# my answer

def fib(number):
    fib_list = []
    for num in range(number + 1):
        if num is 0 or num is 1:
            fib_list.append(num)
        else:
            fib_num = fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2]
            fib_list.append(fib_num)
    print(fib_list)


fib(20)

# answer


def fib2(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib2(20):
    print(x)
