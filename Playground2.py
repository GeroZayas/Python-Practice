def middle_permutation(string):
    s = sorted(string)
    if len(s) % 2 == 0:
        middle_letter = s[len(s) // 2 - 1]
        print(f"this is s[::-1] {s[::-1]}")
        print(f"this is middle_letter if even {middle_letter}")
        return s.pop(len(s) // 2 - 1) + "".join(s[::-1])
    else:
        return s.pop(len(s) // 2) + middle_permutation(s)


s1 = "abc"
s2 = "abcd"
s3 = "abcdx"
s4 = "abcdxg"
s5 = "dczxgba"

r1 = middle_permutation(s1)
r2 = middle_permutation(s2)
r3 = middle_permutation(s3)
r4 = middle_permutation(s4)
r5 = middle_permutation(s5)

print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
