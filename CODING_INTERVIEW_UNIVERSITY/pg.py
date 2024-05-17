import heapq

import random

print(heapq)

# Generate a list of 10 random numbers between 1 and 100
random_numbers = [45, 67, 23, 43, 12, 32, 22]

# Generate a list of 5 random names
random_names = [
    "".join(random.choices("bacategofutru", k=random.randint(5, 10))) for _ in range(5)
]

print("Random numbers:", random_numbers)
print("Random names:", random_names)

heapq.heapify(random_numbers)

print("Heapq random numbers:")
print(random_numbers)
