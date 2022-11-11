# Decorator Practice with Functools
import functools


def multiply_by_10(func):
    @functools.wraps(func)
    def wrapper():
        print("------------------------")
        print(f"This is the number multiplied by 10 => {(func()) * 10}")
        print("------------------------")

    return wrapper


@multiply_by_10
def some_number():
    number = input("insert number ")
    return int(number)


some_number()


print(help(some_number))
print(some_number.__name__)
