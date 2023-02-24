"""
https://pynative.com/python-exercises-with-solutions/

Exercise 8: Create an inner function

Question description: -

Create an outer function that will accept two strings, x and y. (x= 'Emma' and y = 'Kelly'.
Create an inner function inside an outer function that will concatenate x and y.
At last, an outer function will join the word 'developer' to it.

Expected Output: -

EmmaKellyDevelopers

"""


def outer_function(x: str, y: str) -> str:
    def inner_function(z: str, w: str) -> str:
        return z + w

    return inner_function(x, y)


def join_dev_word(x) -> str:
    return x + "Developer"


print(outer_function("Gero", "Zayas"))
print(join_dev_word(outer_function("Gero", "Zayas")))

# Everything in just one function:

print(
    """
Now, another way
Using only one function:
"""
)


def second_outer_function(x: str, y: str) -> str:
    def second_inner_function(z: str, w: str) -> str:
        return z + w

    final_string = second_inner_function(x, y) + "Developer"
    return final_string


my_string = second_outer_function("Gero", "Zayas")
print(my_string)
