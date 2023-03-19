# class decorators act in the same way as a function decorator
# but a class can maintain and update a state


class CountCalls:
    def __init__(self, func):  # class decorator __init__ takes func
        self.func = func
        self.num_calls = 0  # keep tract of how many times func got executed

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("Hello")


say_hello()
# This is executed 1 times
# Hello
say_hello()
# This is executed 2 times
# Hello
say_hello()
# This is executed 3 times
# Hello
