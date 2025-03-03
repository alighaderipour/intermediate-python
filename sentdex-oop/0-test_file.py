import os
os.system('cls' if os.name == 'nt' else 'clear')


def my_decorator(func):
    def wrapper():
        print('something before {}'.format(func.__name__))
        func()
        print('something after {}'.format(func.__name__))
    return wrapper

@my_decorator
def sum_nums(*args):
    return sum(args)

print(sum_nums(1,2,3,4,5,6))