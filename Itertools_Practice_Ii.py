import itertools

# counter = itertools.count()
# print(next(counter))  # 0
# print(next(counter))  # 1
# print(next(counter))  # 2
# print(next(counter))  # 3
# print(next(counter))  # 4
# print(next(counter))  # 5

data = ['a', 'b', 'c', 'd']

# daily_data = list(
#     zip(itertools.count(), data))  # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
# print(daily_data)

# ------------------------------------
counter = itertools.cycle(data)
print(next(counter))  # a
print(next(counter))  # b
print(next(counter))  # c
print(next(counter))  # d
print(next(counter))  # a
print(next(counter))  # b
# ------------------------------------

squares = map(pow, range(10),
              itertools.repeat(2))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(list(squares))

