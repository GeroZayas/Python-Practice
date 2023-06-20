import math
def divide_or_square(num:float)->float:
    if num % 5 == 0:
        return math.sqrt(num)
    else:
        return num % 5

print("Divide of square challege 1:")
print(divide_or_square(10))

