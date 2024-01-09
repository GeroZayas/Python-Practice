# this is from cses.fi/problemset
"""
input: n 

while n > 1:

if n % 2 == 0:
    n = n/2
else:
    n = n * 3 + 1


output: print line with all the outputs with all values of n 
"""


def weird_algo(n):
    result = [
        n,
    ]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            result.append(n)
        else:
            n = (n * 3) + 1
            result.append(n)
    return " ".join(str(n) for n in result)


n = int(input())
print(weird_algo(n))
