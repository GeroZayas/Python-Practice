# create function return random numbers
import random


def choose_random_nums():
    return random.randint(1, 100)


print(choose_random_nums())
