# a function that multiplies all input numbers
def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print(multiply(1, 4, 5))

