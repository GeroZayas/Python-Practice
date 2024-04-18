import heapq

import random

# Generate a list of 10 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(10)]

# Generate a list of 5 random names
random_names = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(5, 10))) for _ in range(5)]

print("Random numbers:", random_numbers)
print("Random names:", random_names)