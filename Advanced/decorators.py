from time import time


def my_decorator(func):
    def wrap_func():
        print('*******')
        func()
        print('*******')
    return wrap_func


@my_decorator
def hello():
    print('hello')


@my_decorator
def bye():
    print('see ya later')


# hello()
# bye()

a = my_decorator(hello)  # this is the alternative to using decorators
# a()

# Using arguments with decorators


def my_decorator2(func):
    def wrap_func(*args, **kwargs):
        print('*******')
        func(*args, **kwargs)
        print('*******')
    return wrap_func


@my_decorator2
def hello2(greeting, emoji=':('):
    print(greeting, emoji)


hello2('hiiii')

# performance decorator


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


long_time()
