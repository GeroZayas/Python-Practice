"""
Task

You are given a string s. Every letter in s appears once.

Consider all strings formed by rearranging the letters in s. After ordering these strings in dictionary order, return the middle term. (If the sequence has a even length n, define its middle term to be the (n/2)th term.)
Example

For s = "abc", the result should be "bac".

 The permutations in order are: "abc", "acb", "bac", "bca", "cab", "cba" So, The middle term is "bac".
Input/Output

    [input] string s

unique letters (2 <= length <= 26)

    [output] a string

middle permutation.
"""
from itertools import permutations

s = "abc"
s2 = "abcd"
s3 = "abcde"


def middle_permutation(string: str):
    r = list(permutations(string))
    print(r)
    middle_perm = ...
    return middle_perm


for s in [s, s2, s3]:
    print(middle_permutation(s), end="\n\n\n")
