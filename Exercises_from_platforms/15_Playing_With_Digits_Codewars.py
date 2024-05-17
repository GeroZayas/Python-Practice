"""
Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1

695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive
powers of p is equal to k * n. In other words:

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

Note: n and p will always be given as strictly positive integers.

dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
"""


def dig_pow(n: int, p: int) -> int:
    k = int
    # We make it a list, so we can take each number separately, but it's a list of strings now
    split_n = list(str(n))
    # We take the list we create, and now we make it a list of integers
    split_n_int = [int(num) for num in split_n]
    # We declare a var sum_total to get hold of the sum of all digits taking to the successive powers of  p
    sum_total = 0
    # We do a for loop to get the sum
    for el in split_n_int:
        sum_total += el**p
        # We increase p by one each time, to make it successive
        p += 1

    # We check in this IF statement if the condition is met
    # If there's no remainder when we divide sum_total by n, then they're divisible
    # and we can get hold of that number, which is the k that we want to return in the function
    if sum_total % n == 0:
        k = int(sum_total / n)
        return k

    return -1


print(dig_pow(89, 1))  # should return 1
print(dig_pow(92, 1))  # should return -1
print(dig_pow(695, 2))  # should return 2
print(dig_pow(46288, 3))  # should return 51
