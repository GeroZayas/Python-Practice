def birthday(s, d, m):
    counter = 0
    if m == 1 and d in s:
        return 1
    for i in range(len(s)-1):
        a_sum = sum(s[i:i+m])
        if a_sum == d:
            counter += 1
    return counter