"""Complete the function that

accepts two integer arrays of equal length

compares the value each member in one array to the corresponding member in the other

squares the absolute value difference between those two values

and returns the average of those squared absolute value difference between each member pair.
"""


def solution(array_a, array_b):
    def subs(a, b):
        return abs(a - b)

    counter = 0

    for e in range(len(array_a)):
        counter += next(map(subs, array_a, array_b)) ** 2
        print("this is counter", (counter))

    return counter / len(array_a)


firstArr, secondArr = [10, 20, 10, 2], [10, 25, 5, -2]

# print(secondArr)

print(solution(firstArr, secondArr))
