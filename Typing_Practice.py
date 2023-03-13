# Importing the `randint` function from the `random` module.
from random import randint

# This is a list comprehension. It is a way to create a list in one line.
num_list_1 = [randint(1, 10) for x in range(11)]
num_list_2 = [randint(1, 10) for x in range(11)]
num_list_3 = [randint(1, 10) for x in range(11)]
# Printing the three lists.
print(num_list_1)
print(num_list_2)
print(num_list_3)


def multiply(a: int, b: int, c: int = 1) -> int:
    """
    `multiply` takes three integers, multiplies them together, and returns the result

    :param a: int - a is a required parameter that must be an integer
    :type a: int
    :param b: int - This is a required parameter
    :type b: int
    :param c: int = 1, defaults to 1
    :type c: int (optional)
    """
    # Multiplying the three numbers together and returning the result.
    return a * b * c


# Using the `map` function to apply the `multiply` function to each element of the three lists.
mult_lists = list(map(multiply, num_list_1, num_list_2, num_list_3))

print(mult_lists)
