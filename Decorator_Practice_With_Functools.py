# Decorator Practice with Functools
import functools


# ------------------------ DECORATORS ------------------------
def multiply_by_10(func):
    @functools.wraps(func)
    def wrapper():
        print("------------------------")
        print(f"This is the number multiplied by 10 => {(func()) * 10}")
        print("------------------------")

    return wrapper


def name_and_repr(func):
    def wrapper(*x):
        return f"the name is '{func.__name__}' and the repr is =>{func.__repr__}"

    return wrapper


# ------------------------ END OF DECORATORS ------------------------


@multiply_by_10
def some_number():
    number = input("insert number ")
    return int(number)


some_number()


# -----------------


@name_and_repr
def greetings(name):
    return f"Hello {name}"


print(greetings("Gero"))
