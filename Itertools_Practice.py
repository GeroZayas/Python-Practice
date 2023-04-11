import itertools
from random import randint

num_list = []

for num in range(10):
    num_list.append(randint(1, 2000))

print(num_list)


selector = [True, False, True, True, False, True, False, True, True, False]

result = itertools.compress(num_list, selectors=selector)

for _ in result:
    print(_)
