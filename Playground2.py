from itertools import permutations


def middle_permutation(string: str):
    sorted_string = sorted(string)
    r = list(permutations(sorted_string))
    middle_perm = "".join(r[int(len(r) / 2) - 1])
    return middle_perm


"""
The problem here is when long strings are added, permutations gets exponentially bigger
How to make more efficiently? namely, how not to actually get all the permutations
just the "necessary" ones to get the wanted result
"""


s1 = "abc"
s2 = "abcd"
s3 = "abcdx"
s4 = "cfryuiljkxns"

r1 = middle_permutation(s1)
r2 = middle_permutation(s2)
r3 = middle_permutation(s3)
r4 = middle_permutation(s4)

print(r1)
print(r2)
print(r3)
print(r4)
