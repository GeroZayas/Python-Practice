from random import randint

num_list_1 = [randint(1, 10) for x in range(11)]
num_list_2 = [randint(1, 10) for x in range(11)]
num_list_3 = [randint(1, 10) for x in range(11)]
print(num_list_1)
print(num_list_2)
print(num_list_3)


def multiply(a: int, b: int, c: int = 1) -> int:
    return a * b * c


mult_lists = list(map(multiply, num_list_1, num_list_2, num_list_3))

print(mult_lists)
