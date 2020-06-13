from time import time


def generator_function(num):
    for i in range(num):
        yield i*2


# for item in generator_function(5):
#     print(item)

g = generator_function(100)
print(next(g))
print(next(g))


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} s')
        return result
    return wrapper


@performance
def long_time():
    for i in range(10000000):
        i*5

# below is slower


def long_time2():
    for i in list(range(10000000)):
        i*5


# long_time()
# long_time2()


def special_for(iterable):
    iterator = iter(iterable)
    print(iterator)
    while True:
        try:
            print(iterator)
            print(next(iterator))
        except StopIteration:
            break


special_for([1, 2, 3])

# this is essentially how generators work


class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
for i in gen:
    print(i)
