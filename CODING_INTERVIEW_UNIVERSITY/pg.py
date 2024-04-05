

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # return sum(ar)
    total = 0
    for n in ar:
        total += n
    return total

print(simpleArraySum([3,4,5]))
