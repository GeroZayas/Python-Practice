import math
def divide_or_square(num:float) -> float:
    return math.sqrt(num) if num % 5 == 0 else num % 5

print("Divide of square challege 1:")
print(divide_or_square(10))

