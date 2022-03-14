def score(x: float, y: float) -> int:
    x, y = abs(x), abs(y)
    sum_pos = x + y
    if x > 5 or y > 5:
        if sum_pos > 14:
            return 0
        return 1
    elif x > 1 or y > 1:
        if sum_pos > 7:
            return 1
        return 5
    elif x >= 0 or y >= 0:
        if sum_pos > 1.4:
            return 5
        return 10
    else:
        return 0


print(score(-3.6, -3.6))  # 1
print(score(7.1, -7.1))  # 0
print(score(-3.5, 3.5))  # 5
print(score(-7.0, 7.0))  # 1
print(score(-5, 0))  # 5
print(score(0.5, -4))  # 5
