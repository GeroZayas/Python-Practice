# Decorators Practice


def hello(func):
    def wrapper():
        str(func) + "Hello"

    return wrapper


@hello
def name():
    name = input("What is your name? ")
    return name
