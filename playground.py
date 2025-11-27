from functools import wraps


def debug(func):
    @wraps(func)
    def out(*args, **kwargs):
        print("function called:", "<", func.__name__, ">")
        return func(*args, **kwargs)

    return out


@debug
def add(x, y):
    return x + y


print(add(4, 5))
