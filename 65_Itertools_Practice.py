from itertools import (
    product,
    permutations,
    combinations,
    combinations_with_replacement,
    accumulate,
    groupby,
)

prod = product([1, 2], [3, 4])
print(list(prod))  # note that we convert the iterator to a list for printing

a = [1, 2, 3]
perm = permutations(a)
print(list(perm))  # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]


# COMBINATIONS FUNCTION
# make all possible combinations with specified length

a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

comb_wr = combinations_with_replacement(a, 2)
print(
    list(comb_wr)
)  # [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

# ACCUMULATE FUNCTION


a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)  # [1, 2, 3, 4]
print(list(acc))  # [1, 3, 6, 10] because 1 + 2 = 3, 3 + 3 = 6, 6 + 4 = 10

a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(list(acc))  # [1, 2, 5, 5, 5], because 5 is the max compared to 3 and 4


# GROUPBY FUNCTION


def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)

for k, v in group_obj:
    print(k, list(v))  # True [1, 2] False [3, 4]


# ------------------------------------------------------

print("*" * 40)

# or use a lamda expression, e.g. words with an 'i':
group_obj = groupby(["hi", "nice", "hello", "cool"], key=lambda x: "i" in x)
for key, group in group_obj:
    print(key, list(group))


# ------------------------------------------------------
print("*" * 40)

persons = [
    {"name": "Tim", "age": 25},
    {"name": "Dan", "age": 25},
    {"name": "Lisa", "age": 27},
    {"name": "Claire", "age": 28},
]


for key, group in groupby(persons, key=lambda x: x["age"]):
    print(key, list(group))

# ------------------------------------------------------
print("*" * 40)
