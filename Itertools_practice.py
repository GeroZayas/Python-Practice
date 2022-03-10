import itertools

counter = itertools.count()
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3

data = ['a', 'b', 'c', 'd']

daily_data = list(
    zip(itertools.count(), data))  # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]

print(daily_data)
